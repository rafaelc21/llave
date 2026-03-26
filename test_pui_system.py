import unittest

from pui_system import PUIService, ValidationError


class TestPUIService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = PUIService()
        self.service.seed_demo_data()

    def test_qr_flow_with_representation_and_audit(self) -> None:
        access = self.service.create_access_request(
            institution_id="sep",
            domain="portal.sep.gob.mx",
            procedure_id="inscripcion_escolar",
            ttl_seconds=120,
        )

        preview = self.service.consent_preview(
            request_id=access.request_id,
            authenticated_user_id="rafael",
            acting_as_id="juan",
            purpose="Inscripcion escolar ciclo 2026",
        )
        self.assertEqual(preview["role"], "tutor")
        self.assertIn("name", preview["shareable_attrs"])
        self.assertIn("tutor_name", preview["shareable_attrs"])

        approval = self.service.approve_consent(
            request_id=access.request_id,
            authenticated_user_id="rafael",
            acting_as_id="juan",
            purpose="Inscripcion escolar ciclo 2026",
            approved_attrs=["name", "curp", "birth_date", "tutor_name"],
        )
        self.assertTrue(approval["approved"])
        self.assertEqual(approval["role"], "tutor")
        self.assertIn("curp", approval["shared_attrs"])
        self.assertIn("tutor_name", approval["shared_attrs"])
        self.assertEqual(len(self.service.audit_events), 1)

        status = self.service.get_request_status(access.request_id)
        self.assertEqual(status["status"], "approved")
        self.assertIn("shared_attrs", status)
        self.assertEqual(status["shared_attrs"]["tutor_name"], "Rafael")

    def test_invalid_domain_is_rejected(self) -> None:
        with self.assertRaises(ValidationError):
            self.service.create_access_request(
                institution_id="sep",
                domain="otro-dominio.gov.mx",
                procedure_id="inscripcion_escolar",
                ttl_seconds=120,
            )

    def test_representation_not_allowed_for_financial(self) -> None:
        access = self.service.create_access_request(
            institution_id="banco",
            domain="demo.banco.mx",
            procedure_id="apertura_cuenta",
            ttl_seconds=120,
        )

        with self.assertRaises(ValidationError):
            self.service.consent_preview(
                request_id=access.request_id,
                authenticated_user_id="rafael",
                acting_as_id="juan",
                purpose="Apertura de cuenta",
            )

    def test_school_enrollment_requires_tutor_context(self) -> None:
        access = self.service.create_access_request(
            institution_id="sep",
            domain="portal.sep.gob.mx",
            procedure_id="inscripcion_escolar",
            ttl_seconds=120,
        )

        with self.assertRaises(ValidationError) as ctx:
            self.service.consent_preview(
                request_id=access.request_id,
                authenticated_user_id="juan",
                acting_as_id="juan",
                purpose="Inscripcion escolar",
            )
        self.assertIn("representacion de un tutor", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
