from __future__ import annotations

from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException

from pui_system import NotFoundError, PUIService, ValidationError


app = Flask(__name__)
service = PUIService()
service.seed_demo_data()


@app.errorhandler(NotFoundError)
def handle_not_found(error: NotFoundError):
    return jsonify({"error": str(error)}), 404


@app.errorhandler(ValidationError)
def handle_validation(error: ValidationError):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(HTTPException)
def handle_http_exception(error: HTTPException):
    return jsonify({"error": error.description}), error.code


@app.errorhandler(Exception)
def handle_general_error(error: Exception):
    return jsonify({"error": f"Error interno: {error}"}), 500


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/")
def root():
    return render_template("demo_web_login.html")


@app.post("/seed")
def reseed():
    global service
    service = PUIService()
    service.seed_demo_data()
    return jsonify({"ok": True, "message": "Datos demo recargados"})


@app.get("/profiles/<device_id>")
def get_profiles(device_id: str):
    profiles = service.get_device_profiles(device_id)
    return jsonify([service.serialize_dataclass(p) for p in profiles])


@app.post("/profiles/assign")
def assign_profile():
    data = request.get_json(force=True)
    service.add_person_to_device(
        device_id=data["device_id"],
        person_id=data["person_id"],
    )
    return jsonify({"ok": True})


@app.get("/contexts/<authenticated_user_id>")
def contexts(authenticated_user_id: str):
    return jsonify(service.context_options(authenticated_user_id))


@app.post("/access-requests")
def create_access_request():
    data = request.get_json(force=True)
    access_request = service.create_access_request(
        institution_id=data["institution_id"],
        domain=data["domain"],
        procedure_id=data["procedure_id"],
        ttl_seconds=int(data.get("ttl_seconds", 180)),
    )
    payload = service.serialize_dataclass(access_request)
    payload["qr_uri"] = f"pui://login?request_id={access_request.request_id}"
    return jsonify(payload), 201


@app.get("/access-requests/<request_id>")
def get_access_request(request_id: str):
    req = service.require_access_request(request_id)
    return jsonify(service.serialize_dataclass(req))


@app.get("/access-requests/<request_id>/status")
def get_access_request_status(request_id: str):
    return jsonify(service.get_request_status(request_id))


@app.post("/consent/preview")
def consent_preview():
    data = request.get_json(force=True)
    preview = service.consent_preview(
        request_id=data["request_id"],
        authenticated_user_id=data["authenticated_user_id"],
        acting_as_id=data["acting_as_id"],
        purpose=data["purpose"],
    )
    return jsonify(preview)


@app.post("/consent/approve")
def consent_approve():
    data = request.get_json(force=True)
    result = service.approve_consent(
        request_id=data["request_id"],
        authenticated_user_id=data["authenticated_user_id"],
        acting_as_id=data["acting_as_id"],
        purpose=data["purpose"],
        approved_attrs=data["approved_attrs"],
        consent_ttl_minutes=int(data.get("consent_ttl_minutes", 15)),
    )
    return jsonify(result)


@app.post("/consent/reject")
def consent_reject():
    data = request.get_json(force=True)
    result = service.reject_consent(
        request_id=data["request_id"],
        authenticated_user_id=data["authenticated_user_id"],
        acting_as_id=data["acting_as_id"],
        reason=data.get("reason", "Rechazado por usuario"),
    )
    return jsonify(result)


@app.get("/audit-events")
def audit_events():
    return jsonify(service.list_audit_events())


@app.get("/demo/web")
def demo_web():
    return render_template("demo_web_login.html")


@app.get("/demo/mobile")
def demo_mobile():
    request_id = request.args.get("request_id", "")
    return render_template("demo_mobile_scan.html", request_id=request_id)


@app.get("/demo/catalog")
def demo_catalog():
    people = [service.serialize_dataclass(p) for p in service.people.values()]
    procedures = [service.serialize_dataclass(p) for p in service.procedures.values()]
    institutions = [service.serialize_dataclass(i) for i in service.institutions.values()]
    return jsonify(
        {
            "people": people,
            "procedures": procedures,
            "institutions": institutions,
            "default_device_id": "device_demo_01",
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
