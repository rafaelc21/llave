# Demo conceptual  
## Plataforma de Identidad Digital Familiar con Acceso Web y Consentimiento Selectivo  
### Evolución de identidad digital para gobierno

---

## 1. Nombre de la propuesta

**Plataforma de Identidad Digital Familiar y Representación Digital (PUI)**

---

## 2. Propósito del demo

Demostrar un modelo de identidad digital que:

- permite autenticación segura en móvil y web;
- soporta múltiples personas en un mismo dispositivo;
- habilita representación (tutor, familiar, autorizado);
- permite acceso web mediante QR seguro;
- comparte datos de forma selectiva por trámite;
- registra trazabilidad completa.

---

## 3. Problema que atiende

Los sistemas actuales funcionan bajo:

**1 persona = 1 cuenta = 1 acceso**

Pero la realidad incluye:

- padres gestionando trámites de hijos;
- familiares apoyando adultos mayores;
- uso compartido de dispositivos;
- necesidad de actuar por otros legalmente.

Esto genera:
- compartición de contraseñas;
- falta de trazabilidad;
- errores de identidad;
- mala experiencia digital.

---

## 4. Objetivo

Crear un sistema donde:

- una persona se autentica;
- puede actuar por sí misma o por otros;
- el sistema valida esa representación;
- y comparte solo los datos necesarios.

---

## 5. Concepto clave

**Identidad + Relación + Contexto + Consentimiento**

---

## 6. Componentes del modelo

### 6.1 Persona
- identificador único
- nombre
- CURP
- fecha de nacimiento

---

### 6.2 Perfil
- identidad usable en dispositivo
- método de acceso (biometría / PIN)

---

### 6.3 Relación
Define vínculos:

- tutor → hijo
- cónyuge → cónyuge
- autorizado → representado

Incluye:
- tipo
- vigencia
- permisos

---

### 6.4 Institución
- nombre
- dominio web autorizado
- tipo (salud, educación, financiero)
- certificados de confianza

---

### 6.5 Trámite
- nombre
- institución
- atributos requeridos
- si permite representación

---

### 6.6 Solicitud de acceso
- request_id
- institución
- dominio
- tipo de acceso
- expiración

---

### 6.7 Consentimiento
- atributos aprobados
- finalidad
- vigencia

---

### 6.8 Evento de auditoría
- quién se autenticó
- por quién actuó
- qué hizo
- cuándo

---

## 7. Alta de entidades

El sistema incluye el registro de:

### 7.1 Personas
Ejemplo:
- Rafael
- Juan (hijo)

---

### 7.2 Relaciones
Ejemplo:

- Rafael → tutor de Juan  
- alcance: educación, salud  
- vigencia: activa  

---

### 7.3 Instituciones
Ejemplo:

- SEP  
- IMSS  
- Banco  

---

### 7.4 Trámites
Ejemplo:

- inscripción escolar  
- cita médica  
- apertura de cuenta  

---

### 7.5 Reglas por trámite

Definen:

- datos obligatorios  
- datos opcionales  
- si permite representación  

---

## 8. Acceso web con QR

---

### 8.1 Concepto

Acceso web mediante QR similar a WhatsApp Web, pero con:

- validación de identidad
- selección de contexto
- verificación de representación

---

### 8.2 Flujo completo

---

#### Paso 1. Usuario entra al portal web

Ejemplo:
- portal escolar

Botón:

**Entrar con identidad digital**

---

#### Paso 2. El backend genera solicitud

Ejemplo:

```json
{
  "request_id": "REQ123",
  "institution": "SEP",
  "domain": "portal.sep.gob.mx",
  "expires_at": "2026-03-24T14:12:00Z"
}

Paso 3. Se muestra QR
pui://login?request_id=REQ123
Paso 4. Usuario escanea con app

La app muestra:

institución
dominio
tipo de acceso
Paso 5. Selección de contexto

Opciones:

Actuar como Rafael
Actuar como tutor de Juan
Paso 6. Autenticación
biometría (huella o rostro)
PIN (si es necesario)
Paso 7. Validación

El sistema valida:

identidad del usuario
relación con la persona
permiso para el trámite
dominio autorizado
Paso 8. Respuesta al servidor
{
  "authenticated_user": "Rafael",
  "acting_as": "Juan",
  "role": "tutor",
  "approved": true
}
Paso 9. Inicio de sesión

La web muestra:

Sesión activa: Rafael actuando como tutor de Juan

9. Qué valida el sistema

El acceso QR valida:

identidad real del usuario
autenticación biométrica
relación válida
permiso de representación
contexto correcto
10. Compartición selectiva de datos
Ejemplo: inscripción escolar

Se comparte:

nombre del menor
CURP
fecha de nacimiento
tutor

No se comparte:

datos bancarios
datos médicos
Pantalla de consentimiento

Institución: SEP
Trámite: Inscripción escolar
Persona: Juan

Datos:

nombre
CURP
fecha de nacimiento
tutor
11. UX del sistema
11.1 Selección de perfil
lista de personas
11.2 Dashboard
identidad activa
servicios
familia
11.3 Cambio de contexto
actuar como yo
actuar como dependiente
11.4 Indicador visible

Siempre mostrar:

Actuando como: Juan

11.5 Historial

Ejemplo:

Rafael actuó como Juan → inscripción escolar
12. Seguridad
Capas
biometría
PIN
validación de dominio
expiración de QR
auditoría
Prevención
no uso de contraseñas
no compartir cuentas
protección contra phishing
13. Beneficios
Para gobierno
mayor control
mejor trazabilidad
reducción de fraude
interoperabilidad
Para ciudadanía
uso familiar real
menos fricción
control de datos
mejor experiencia
14. Diferenciador clave

Este modelo no solo autentica:

👉 valida identidad + contexto + representación

15. Frase de cierre

El acceso digital no debe validar solo quién eres, sino también en qué contexto actúas y con qué facultades.