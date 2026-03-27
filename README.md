# Plataforma PUI - MVP backend

Este proyecto implementa un MVP funcional basado en `segunda_propuesta.md` y `especificacion.md`.

Incluye:

- gestion de personas y perfiles por dispositivo;
- relaciones de representacion (tutor/autorizado);
- solicitudes de acceso web por QR (`request_id`);
- seleccion de contexto (actuar como yo / actuar por otra persona);
- consentimiento contextual y comparticion selectiva de atributos;
- auditoria de eventos.

## Arquitectura (MVP)

- `server.py`: API REST en Flask.
- `pui_system.py`: logica de negocio, validaciones y modelo en memoria.
- `test_pui_system.py`: pruebas del flujo principal.

## Requisitos

- Python 3.10+ recomendado.

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
python server.py
```

Servidor por defecto: `http://127.0.0.1:8000`

## Endpoints principales

- `GET /health`
- `POST /seed`
- `GET /profiles/<device_id>`
- `POST /profiles/assign`
- `GET /contexts/<authenticated_user_id>`
- `POST /access-requests`
- `GET /access-requests/<request_id>`
- `GET /access-requests/<request_id>/status`
- `POST /consent/preview`
- `POST /consent/approve`
- `POST /consent/reject`
- `GET /audit-events`

## Demo visual (portal + movil)

Una vez levantado el servidor, abre:

- Portal web: `http://127.0.0.1:8000/demo/web`
- Pantalla movil: `http://127.0.0.1:8000/demo/mobile`

Flujo recomendado:

1. En `demo/web`, selecciona institucion/tramite y presiona **Generar QR**.
2. Escanea el QR con el celular (o abre el link mostrado).
3. En `demo/mobile`, carga la solicitud, elige usuario/contexto y aprueba.
4. Regresa a `demo/web`: la sesion cambia a **aprobado** automaticamente por polling.

### Boton "Agregar a Google Wallet" (demo)

La pantalla `demo/mobile` ya incluye el boton **Agregar a Google Wallet**.

Para habilitarlo, define esta variable de entorno en tu servidor:

- `GOOGLE_WALLET_SAVE_URL_TEMPLATE`

Valor esperado: URL final de guardado de Google Wallet (normalmente `https://pay.google.com/gp/v/save/<JWT>`).

Si no esta configurada, el sistema mostrara un mensaje indicando que falta la configuracion.

## Flujo de ejemplo (inscripcion escolar)

1) Crear solicitud QR:

```bash
curl -X POST http://127.0.0.1:8000/access-requests ^
  -H "Content-Type: application/json" ^
  -d "{\"institution_id\":\"sep\",\"domain\":\"portal.sep.gob.mx\",\"procedure_id\":\"inscripcion_escolar\"}"
```

2) Previsualizar consentimiento con contexto tutor:

```bash
curl -X POST http://127.0.0.1:8000/consent/preview ^
  -H "Content-Type: application/json" ^
  -d "{\"request_id\":\"REQ-XXXXX\",\"authenticated_user_id\":\"rafael\",\"acting_as_id\":\"juan\",\"purpose\":\"Inscripcion escolar\"}"
```

3) Aprobar consentimiento (solo atributos requeridos):

```bash
curl -X POST http://127.0.0.1:8000/consent/approve ^
  -H "Content-Type: application/json" ^
  -d "{\"request_id\":\"REQ-XXXXX\",\"authenticated_user_id\":\"rafael\",\"acting_as_id\":\"juan\",\"purpose\":\"Inscripcion escolar\",\"approved_attrs\":[\"name\",\"curp\",\"birth_date\",\"tutor_name\"]}"
```

4) Ver auditoria:

```bash
curl http://127.0.0.1:8000/audit-events
```

## Pruebas

```bash
python -m unittest test_pui_system.py -v
```

## Siguientes pasos recomendados

- persistencia real (PostgreSQL);
- autenticacion fuerte (OIDC + WebAuthn/biometria en cliente);
- firma de consentimientos y versionado de politicas;
- engine de reglas configurable por institucion/tramite;
- integracion con portal web real para QR login.
