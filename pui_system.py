from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


@dataclass
class Person:
    person_id: str
    name: str
    curp: str
    birth_date: str
    person_type: str = "individual"


@dataclass
class Relationship:
    relationship_id: str
    actor_id: str
    target_id: str
    role: str
    scopes: list[str]
    valid_from: datetime
    valid_to: datetime
    active: bool = True

    def is_valid_now(self, now: datetime) -> bool:
        return self.active and self.valid_from <= now <= self.valid_to


@dataclass
class Institution:
    institution_id: str
    name: str
    domain: str
    institution_type: str
    trust_certificate: str


@dataclass
class Procedure:
    procedure_id: str
    institution_id: str
    name: str
    scope: str
    required_attrs: list[str]
    optional_attrs: list[str]
    allows_representation: bool


@dataclass
class AccessRequest:
    request_id: str
    institution_id: str
    domain: str
    procedure_id: str
    expires_at: datetime
    access_type: str = "web_qr"
    status: str = "pending"

    def is_expired(self, now: datetime) -> bool:
        return now > self.expires_at


@dataclass
class ConsentRecord:
    consent_id: str
    request_id: str
    approved: bool
    approved_attrs: list[str]
    purpose: str
    expires_at: datetime
    authenticated_user_id: str
    acting_as_id: str
    role: str
    created_at: datetime


@dataclass
class AuditEvent:
    event_id: str
    timestamp: datetime
    authenticated_user_id: str
    acting_as_id: str
    action: str
    institution_id: str
    procedure_id: str
    shared_attrs: dict[str, Any]
    details: dict[str, Any] = field(default_factory=dict)


class PUIError(Exception):
    pass


class NotFoundError(PUIError):
    pass


class ValidationError(PUIError):
    pass


class PUIService:
    def __init__(self) -> None:
        self.people: dict[str, Person] = {}
        self.relationships: dict[str, Relationship] = {}
        self.institutions: dict[str, Institution] = {}
        self.procedures: dict[str, Procedure] = {}
        self.access_requests: dict[str, AccessRequest] = {}
        self.consents: dict[str, ConsentRecord] = {}
        self.audit_events: list[AuditEvent] = []
        self.device_profiles: dict[str, list[str]] = {}

    def seed_demo_data(self) -> None:
        now = utc_now()
        in_two_years = now + timedelta(days=365 * 2)

        self.people["rafael"] = Person(
            person_id="rafael",
            name="Rafael",
            curp="RAFA900101HDFABC01",
            birth_date="1990-01-01",
        )
        self.people["juan"] = Person(
            person_id="juan",
            name="Juan",
            curp="JUAN150430HDFABC02",
            birth_date="2015-04-30",
        )
        self.people["maria"] = Person(
            person_id="maria",
            name="Maria",
            curp="MARI420710MDFABC03",
            birth_date="1942-07-10",
        )

        self.relationships["rel_tutor_juan"] = Relationship(
            relationship_id="rel_tutor_juan",
            actor_id="rafael",
            target_id="juan",
            role="tutor",
            scopes=["education", "health"],
            valid_from=now - timedelta(days=30),
            valid_to=in_two_years,
        )
        self.relationships["rel_autorizado_maria"] = Relationship(
            relationship_id="rel_autorizado_maria",
            actor_id="rafael",
            target_id="maria",
            role="authorized",
            scopes=["social_programs"],
            valid_from=now - timedelta(days=30),
            valid_to=in_two_years,
        )

        self.institutions["sep"] = Institution(
            institution_id="sep",
            name="SEP",
            domain="portal.sep.gob.mx",
            institution_type="education",
            trust_certificate="CERT-SEP-001",
        )
        self.institutions["imss"] = Institution(
            institution_id="imss",
            name="IMSS",
            domain="citas.imss.gob.mx",
            institution_type="health",
            trust_certificate="CERT-IMSS-001",
        )
        self.institutions["banco"] = Institution(
            institution_id="banco",
            name="Banco Demo",
            domain="demo.banco.mx",
            institution_type="financial",
            trust_certificate="CERT-BANCO-001",
        )

        self.procedures["inscripcion_escolar"] = Procedure(
            procedure_id="inscripcion_escolar",
            institution_id="sep",
            name="Inscripcion escolar",
            scope="education",
            required_attrs=["name", "curp", "birth_date", "tutor_name"],
            optional_attrs=[],
            allows_representation=True,
        )
        self.procedures["cita_medica"] = Procedure(
            procedure_id="cita_medica",
            institution_id="imss",
            name="Cita medica",
            scope="health",
            required_attrs=["name", "curp", "birth_date", "guardian_contact"],
            optional_attrs=["emergency_phone"],
            allows_representation=True,
        )
        self.procedures["apertura_cuenta"] = Procedure(
            procedure_id="apertura_cuenta",
            institution_id="banco",
            name="Apertura de cuenta",
            scope="financial",
            required_attrs=["name", "curp", "birth_date", "is_adult"],
            optional_attrs=["address"],
            allows_representation=False,
        )

        self.device_profiles["device_demo_01"] = ["rafael", "juan", "maria"]

    def add_person_to_device(self, device_id: str, person_id: str) -> None:
        self.require_person(person_id)
        profiles = self.device_profiles.setdefault(device_id, [])
        if person_id not in profiles:
            profiles.append(person_id)

    def get_device_profiles(self, device_id: str) -> list[Person]:
        person_ids = self.device_profiles.get(device_id, [])
        return [self.people[p_id] for p_id in person_ids if p_id in self.people]

    def create_access_request(
        self,
        institution_id: str,
        domain: str,
        procedure_id: str,
        ttl_seconds: int = 180,
    ) -> AccessRequest:
        institution = self.require_institution(institution_id)
        procedure = self.require_procedure(procedure_id)

        if institution.domain != domain:
            raise ValidationError("Dominio no autorizado para la institucion.")
        if procedure.institution_id != institution_id:
            raise ValidationError("El tramite no pertenece a la institucion indicada.")
        if ttl_seconds <= 0:
            raise ValidationError("ttl_seconds debe ser mayor a cero.")

        request_id = f"REQ-{uuid4().hex[:10].upper()}"
        access_request = AccessRequest(
            request_id=request_id,
            institution_id=institution_id,
            domain=domain,
            procedure_id=procedure_id,
            expires_at=utc_now() + timedelta(seconds=ttl_seconds),
        )
        self.access_requests[request_id] = access_request
        return access_request

    def context_options(self, authenticated_user_id: str) -> list[dict[str, str]]:
        user = self.require_person(authenticated_user_id)
        options = [
            {
                "acting_as": user.person_id,
                "role": "self",
                "label": f"Actuar como {user.name}",
            }
        ]
        now = utc_now()
        for rel in self.relationships.values():
            if rel.actor_id != authenticated_user_id or not rel.is_valid_now(now):
                continue
            target = self.require_person(rel.target_id)
            options.append(
                {
                    "acting_as": target.person_id,
                    "role": rel.role,
                    "label": f"Actuar como {rel.role} de {target.name}",
                }
            )
        return options

    def consent_preview(
        self,
        request_id: str,
        authenticated_user_id: str,
        acting_as_id: str,
        purpose: str,
    ) -> dict[str, Any]:
        access_request = self.require_access_request(request_id)
        procedure = self.require_procedure(access_request.procedure_id)
        institution = self.require_institution(access_request.institution_id)

        if access_request.is_expired(utc_now()):
            raise ValidationError("La solicitud ya expiro.")
        if access_request.status != "pending":
            raise ValidationError("La solicitud ya fue procesada.")

        role = self.validate_representation(
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            procedure_id=procedure.procedure_id,
        )

        if "tutor_name" in procedure.required_attrs and role == "self":
            raise ValidationError(
                "Este tramite requiere actuar en representacion de un tutor. "
                "Selecciona un usuario tutor y el contexto de representacion."
            )

        person_attrs = self.person_attributes(
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
        )

        requested = procedure.required_attrs + procedure.optional_attrs
        shareable_attrs = {k: person_attrs[k] for k in requested if k in person_attrs}
        blocked_attrs = [k for k in requested if k not in shareable_attrs]
        missing_required = [
            attr for attr in procedure.required_attrs if attr not in shareable_attrs
        ]
        if missing_required:
            raise ValidationError(
                "El contexto seleccionado no puede compartir atributos obligatorios: "
                f"{missing_required}. Cambia de contexto o usuario."
            )

        return {
            "request_id": access_request.request_id,
            "institution": institution.name,
            "domain": institution.domain,
            "procedure": procedure.name,
            "authenticated_user_id": authenticated_user_id,
            "acting_as_id": acting_as_id,
            "role": role,
            "purpose": purpose,
            "required_attrs": procedure.required_attrs,
            "optional_attrs": procedure.optional_attrs,
            "shareable_attrs": shareable_attrs,
            "blocked_attrs": blocked_attrs,
            "expires_at": iso(access_request.expires_at),
        }

    def approve_consent(
        self,
        request_id: str,
        authenticated_user_id: str,
        acting_as_id: str,
        purpose: str,
        approved_attrs: list[str],
        consent_ttl_minutes: int = 15,
    ) -> dict[str, Any]:
        preview = self.consent_preview(
            request_id=request_id,
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            purpose=purpose,
        )
        available = set(preview["shareable_attrs"].keys())
        requested_required = set(preview["required_attrs"])

        selected = set(approved_attrs)
        if not requested_required.issubset(selected):
            missing = sorted(requested_required - selected)
            raise ValidationError(
                f"Faltan atributos obligatorios en consentimiento: {missing}"
            )
        if not selected.issubset(available):
            invalid = sorted(selected - available)
            raise ValidationError(
                f"Atributos no disponibles para compartir: {invalid}"
            )

        request_obj = self.require_access_request(request_id)
        consent_id = f"CONS-{uuid4().hex[:10].upper()}"
        record = ConsentRecord(
            consent_id=consent_id,
            request_id=request_id,
            approved=True,
            approved_attrs=sorted(selected),
            purpose=purpose,
            expires_at=utc_now() + timedelta(minutes=consent_ttl_minutes),
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            role=preview["role"],
            created_at=utc_now(),
        )
        self.consents[consent_id] = record
        request_obj.status = "approved"

        shared_payload = {
            key: value
            for key, value in preview["shareable_attrs"].items()
            if key in selected
        }

        event = AuditEvent(
            event_id=f"AUD-{uuid4().hex[:10].upper()}",
            timestamp=utc_now(),
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            action="consent_approved",
            institution_id=request_obj.institution_id,
            procedure_id=request_obj.procedure_id,
            shared_attrs=shared_payload,
            details={
                "request_id": request_id,
                "consent_id": consent_id,
                "purpose": purpose,
            },
        )
        self.audit_events.append(event)

        return {
            "request_id": request_id,
            "approved": True,
            "consent_id": consent_id,
            "authenticated_user": authenticated_user_id,
            "acting_as": acting_as_id,
            "role": preview["role"],
            "shared_attrs": shared_payload,
            "session_message": self.build_session_message(
                authenticated_user_id=authenticated_user_id,
                acting_as_id=acting_as_id,
                role=preview["role"],
            ),
        }

    def reject_consent(
        self,
        request_id: str,
        authenticated_user_id: str,
        acting_as_id: str,
        reason: str,
    ) -> dict[str, Any]:
        access_request = self.require_access_request(request_id)
        if access_request.is_expired(utc_now()):
            raise ValidationError("La solicitud ya expiro.")
        if access_request.status != "pending":
            raise ValidationError("La solicitud ya fue procesada.")

        _ = self.validate_representation(
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            procedure_id=access_request.procedure_id,
        )
        access_request.status = "rejected"

        event = AuditEvent(
            event_id=f"AUD-{uuid4().hex[:10].upper()}",
            timestamp=utc_now(),
            authenticated_user_id=authenticated_user_id,
            acting_as_id=acting_as_id,
            action="consent_rejected",
            institution_id=access_request.institution_id,
            procedure_id=access_request.procedure_id,
            shared_attrs={},
            details={"request_id": request_id, "reason": reason},
        )
        self.audit_events.append(event)
        return {"request_id": request_id, "approved": False, "reason": reason}

    def validate_representation(
        self, authenticated_user_id: str, acting_as_id: str, procedure_id: str
    ) -> str:
        self.require_person(authenticated_user_id)
        self.require_person(acting_as_id)
        procedure = self.require_procedure(procedure_id)

        if authenticated_user_id == acting_as_id:
            return "self"

        if not procedure.allows_representation:
            raise ValidationError("Este tramite no permite representacion.")

        now = utc_now()
        valid_relationship = None
        for rel in self.relationships.values():
            if (
                rel.actor_id == authenticated_user_id
                and rel.target_id == acting_as_id
                and rel.is_valid_now(now)
                and procedure.scope in rel.scopes
            ):
                valid_relationship = rel
                break

        if not valid_relationship:
            raise ValidationError(
                "No existe una relacion valida para actuar en este contexto."
            )

        return valid_relationship.role

    def person_attributes(
        self, authenticated_user_id: str, acting_as_id: str
    ) -> dict[str, Any]:
        person = self.require_person(acting_as_id)
        auth_user = self.require_person(authenticated_user_id)
        is_adult = self.calculate_age(person.birth_date) >= 18

        attrs: dict[str, Any] = {
            "name": person.name,
            "curp": person.curp,
            "birth_date": person.birth_date,
            "is_adult": is_adult,
            "guardian_contact": auth_user.name if authenticated_user_id != acting_as_id else "",
            "emergency_phone": "+52-555-000-0000",
            "address": "CDMX, Mexico",
        }

        if authenticated_user_id != acting_as_id:
            attrs["tutor_name"] = auth_user.name
        return attrs

    @staticmethod
    def build_session_message(
        authenticated_user_id: str, acting_as_id: str, role: str
    ) -> str:
        if role == "self":
            return f"Sesion activa: {authenticated_user_id} actuando como si mismo"
        return (
            f"Sesion activa: {authenticated_user_id} actuando como "
            f"{role} de {acting_as_id}"
        )

    @staticmethod
    def calculate_age(birth_date: str) -> int:
        year, month, day = [int(v) for v in birth_date.split("-")]
        born = datetime(year=year, month=month, day=day, tzinfo=timezone.utc).date()
        today = utc_now().date()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def require_person(self, person_id: str) -> Person:
        person = self.people.get(person_id)
        if not person:
            raise NotFoundError(f"Persona no encontrada: {person_id}")
        return person

    def require_institution(self, institution_id: str) -> Institution:
        institution = self.institutions.get(institution_id)
        if not institution:
            raise NotFoundError(f"Institucion no encontrada: {institution_id}")
        return institution

    def require_procedure(self, procedure_id: str) -> Procedure:
        procedure = self.procedures.get(procedure_id)
        if not procedure:
            raise NotFoundError(f"Tramite no encontrado: {procedure_id}")
        return procedure

    def require_access_request(self, request_id: str) -> AccessRequest:
        request_obj = self.access_requests.get(request_id)
        if not request_obj:
            raise NotFoundError(f"Solicitud no encontrada: {request_id}")
        return request_obj

    def get_consent_by_request(self, request_id: str) -> ConsentRecord | None:
        for consent in self.consents.values():
            if consent.request_id == request_id:
                return consent
        return None

    def get_approved_audit_event_by_request(self, request_id: str) -> AuditEvent | None:
        for event in reversed(self.audit_events):
            if (
                event.action == "consent_approved"
                and event.details.get("request_id") == request_id
            ):
                return event
        return None

    def get_request_status(self, request_id: str) -> dict[str, Any]:
        request_obj = self.require_access_request(request_id)
        result: dict[str, Any] = {
            "request_id": request_obj.request_id,
            "status": request_obj.status,
            "expires_at": iso(request_obj.expires_at),
        }

        consent = self.get_consent_by_request(request_id)
        if not consent:
            return result

        result["consent"] = {
            "consent_id": consent.consent_id,
            "approved": consent.approved,
            "approved_attrs": consent.approved_attrs,
            "authenticated_user_id": consent.authenticated_user_id,
            "acting_as_id": consent.acting_as_id,
            "role": consent.role,
            "purpose": consent.purpose,
            "expires_at": iso(consent.expires_at),
        }
        event = self.get_approved_audit_event_by_request(request_id)
        result["shared_attrs"] = event.shared_attrs if event else {}
        result["session_message"] = self.build_session_message(
            authenticated_user_id=consent.authenticated_user_id,
            acting_as_id=consent.acting_as_id,
            role=consent.role,
        )
        return result

    def serialize_dataclass(self, obj: Any) -> dict[str, Any]:
        data = asdict(obj)
        for key, value in list(data.items()):
            if isinstance(value, datetime):
                data[key] = iso(value)
        return data

    def list_audit_events(self) -> list[dict[str, Any]]:
        serialized: list[dict[str, Any]] = []
        for event in self.audit_events:
            item = self.serialize_dataclass(event)
            serialized.append(item)
        return serialized
