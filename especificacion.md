\# Demo conceptual  

\## Plataforma de Identidad Digital Familiar con Consentimiento Selectivo  

\### Propuesta de evolución de identidad digital para gobierno



\---



\## 1. Nombre de la propuesta



\*\*Plataforma de Identidad Digital Familiar y Representación Digital\*\*  

\*\*(PUI – Personal Unique Interface / Wallet de identidad)\*\*



\---



\## 2. Propósito del demo



Presentar un modelo conceptual de identidad digital centrado en la persona, que permita:



\- autenticación segura para ciudadanía;

\- representación digital de hijas, hijos y dependientes;

\- uso de un mismo dispositivo con múltiples perfiles;

\- consentimiento explícito y compartición selectiva de datos según institución y trámite;

\- trazabilidad completa de quién realizó una acción y en representación de quién.



Este demo busca ilustrar una posible evolución de los esquemas actuales de identidad digital hacia un modelo más flexible, familiar, interoperable y seguro.



\---



\## 3. Problema público que atiende



Actualmente, muchos trámites digitales están diseñados bajo una lógica de:



\*\*1 identidad = 1 persona = 1 acceso\*\*



Sin embargo, en la práctica, existen múltiples escenarios donde una persona requiere actuar por otra, por ejemplo:



\- madre o padre que realiza trámites por hijos menores;

\- personas cuidadoras que apoyan a adultos mayores;

\- tutores legales;

\- cónyuges con autorizaciones acotadas;

\- personas con baja alfabetización digital;

\- familias que utilizan un mismo dispositivo móvil.



Esto genera problemas como:



\- uso incorrecto de cuentas ajenas;

\- compartición de contraseñas;

\- falta de trazabilidad;

\- riesgos de seguridad;

\- mala experiencia de usuario;

\- limitaciones para implementar servicios digitales familiares.



\---



\## 4. Objetivo general



Diseñar y demostrar una solución de identidad digital que permita a una persona autenticarse de forma segura y, cuando corresponda, actuar en representación de otra persona con autorización o vínculo legal válido, compartiendo únicamente los datos estrictamente necesarios para cada trámite.



\---



\## 5. Objetivos específicos



\- habilitar perfiles múltiples dentro de un mismo dispositivo;

\- permitir cambio de contexto entre identidad propia y representación;

\- incorporar autenticación reforzada mediante biometría y PIN;

\- aplicar reglas de consentimiento por institución, trámite y persona objetivo;

\- mostrar al usuario qué datos se compartirán y con qué finalidad;

\- registrar de forma auditable cada acción realizada.



\---



\## 6. Concepto rector



\### Identidad + representación + consentimiento contextual



La propuesta no sustituye el concepto de identidad individual, sino que lo amplía mediante una capa adicional de:



\- \*\*representación digital\*\*;

\- \*\*delegación controlada\*\*;

\- \*\*consentimiento por trámite\*\*;

\- \*\*divulgación selectiva de atributos\*\*.



\---



\## 7. Principios de diseño



\### 7.1 Centrado en la persona

La identidad digital debe construirse alrededor de la persona y sus relaciones reales.



\### 7.2 Claridad de contexto

Siempre debe quedar claro:

\- quién está autenticado;

\- por quién está actuando;

\- qué trámite está realizando.



\### 7.3 Mínima divulgación

La plataforma solo compartirá los datos estrictamente necesarios para el trámite.



\### 7.4 Seguridad por capas

Cada operación deberá protegerse con autenticación adecuada al riesgo.



\### 7.5 Interoperabilidad

La solución debe poder integrarse con instituciones públicas y privadas.



\### 7.6 Trazabilidad

Toda acción debe quedar registrada con evidencia suficiente.



\---



\## 8. Casos de uso prioritarios



\### 8.1 Madre o padre realiza inscripción escolar de un hijo

\- inicia sesión con su identidad;

\- selecciona actuar como tutor del menor;

\- autoriza compartir datos del menor con la institución educativa;

\- el sistema registra que el trámite fue realizado por el tutor.



\### 8.2 Tutor agenda cita médica para un menor

\- el tutor accede con su perfil;

\- cambia al contexto del menor;

\- comparte únicamente los datos necesarios para salud;

\- se registra el parentesco o facultad de representación.



\### 8.3 Persona adulta mayor es asistida por familiar autorizado

\- el familiar entra con su identidad;

\- actúa mediante delegación expresa;

\- consulta o realiza un trámite autorizado;

\- no se exponen otros datos no necesarios.



\### 8.4 Uso de un mismo teléfono por varios miembros de la familia

\- el dispositivo contiene varios perfiles;

\- cada uno accede mediante biometría y/o PIN;

\- los datos se mantienen separados por perfil;

\- el sistema diferencia identidad propia y representación.



\---



\## 9. Propuesta funcional del demo



El demo muestra una aplicación móvil de identidad digital familiar con las siguientes capacidades:



\### 9.1 Múltiples perfiles en un mismo dispositivo

Ejemplo:

\- Rafael

\- Ana

\- Juan

\- María



\### 9.2 Inicio de sesión por perfil

Cada perfil puede ingresar mediante:

\- huella;

\- rostro;

\- PIN del perfil.



\### 9.3 Cambio de contexto

La app permite elegir entre:

\- actuar como yo;

\- actuar como tutor de un menor;

\- actuar en representación de una persona autorizada.



\### 9.4 Consentimiento contextual

Antes de compartir datos, la app muestra:

\- institución solicitante;

\- trámite;

\- persona objetivo;

\- datos que se compartirán;

\- finalidad.



\### 9.5 Compartición selectiva de datos

La app comparte solo atributos autorizados para ese trámite.



\### 9.6 Registro auditable

Cada acción deja evidencia de:

\- persona autenticada;

\- persona representada;

\- institución;

\- trámite;

\- atributos compartidos;

\- fecha y hora.



\---



\## 10. Ejemplo de experiencia de usuario



\### Escenario: inscripción escolar de un menor



\#### Paso 1. Selección de perfil

Pantalla inicial:

\- Rafael

\- Ana

\- Juan

\- María



El usuario selecciona: \*\*Rafael\*\*



\#### Paso 2. Autenticación

La app solicita:

\- huella o rostro;

\- en caso de operación sensible, PIN adicional.



\#### Paso 3. Selección de contexto

La app muestra:

\- Actuar como Rafael

\- Actuar como tutor de Juan

\- Actuar como tutor de María



El usuario selecciona: \*\*Actuar como tutor de Juan\*\*



\#### Paso 4. Confirmación de contexto

Mensaje visible:



> Estás actuando como tutor de Juan



\#### Paso 5. Solicitud de datos por institución

La app muestra:



\*\*Institución:\*\* Secretaría de Educación  

\*\*Trámite:\*\* Inscripción escolar  

\*\*Persona objetivo:\*\* Juan  

\*\*Datos requeridos:\*\*  

\- nombre completo del menor;  

\- CURP del menor;  

\- fecha de nacimiento;  

\- nombre del tutor.



\*\*No se compartirán:\*\*  

\- datos bancarios;  

\- historial médico;  

\- otros documentos no relacionados.



\#### Paso 6. Consentimiento

Botones:

\- Aprobar

\- Rechazar

\- Ver detalle



\#### Paso 7. Envío de atributos

La app comparte únicamente los datos necesarios.



\#### Paso 8. Resultado y trazabilidad

Se registra:



> Rafael actuó como tutor de Juan en trámite de inscripción escolar ante la institución educativa correspondiente.



\---



\## 11. Pantallas incluidas en el demo



\### 11.1 Pantalla de selección de perfiles

Objetivo:

\- seleccionar quién usará el dispositivo.



\### 11.2 Pantalla de autenticación

Objetivo:

\- validar identidad del perfil activo.



\### 11.3 Dashboard principal

Objetivo:

\- mostrar identidad activa y accesos rápidos.



Elementos:

\- encabezado de contexto;

\- identidad;

\- documentos;

\- servicios;

\- familia;

\- seguridad.



\### 11.4 Pantalla de cambio de contexto

Objetivo:

\- pasar de identidad propia a representación.



\### 11.5 Pantalla de consentimiento por trámite

Objetivo:

\- mostrar de forma clara qué se compartirá.



\### 11.6 Pantalla de resultado

Objetivo:

\- confirmar acción realizada y registrar trazabilidad.



\### 11.7 Historial de actividades

Objetivo:

\- consultar quién hizo qué, por quién y cuándo.



\---



\## 12. Arquitectura conceptual



La solución se compone de cinco capas:



\### 12.1 Capa de identidad

Administra:

\- identidad base de la persona;

\- autenticación;

\- perfiles.



\### 12.2 Capa de representación

Administra:

\- tutoría;

\- patria potestad;

\- delegaciones autorizadas;

\- vigencias y alcances.



\### 12.3 Capa de consentimiento

Administra:

\- solicitudes por institución;

\- finalidades;

\- atributos requeridos;

\- aceptación o rechazo.



\### 12.4 Capa de intercambio de atributos

Comparte:

\- solo los datos autorizados;

\- de forma estructurada;

\- por trámite y contexto.



\### 12.5 Capa de auditoría

Registra:

\- evento;

\- identidad autenticada;

\- representación;

\- datos compartidos;

\- evidencias.



\---



\## 13. Componentes del sistema



\### 13.1 App móvil de identidad

Funcionalidades:

\- perfiles;

\- acceso biométrico;

\- cambio de contexto;

\- consentimiento;

\- historial.



\### 13.2 Motor de reglas

Define:

\- qué institución puede pedir qué datos;

\- para qué trámite;

\- bajo qué condiciones;

\- si permite representación.



\### 13.3 Backend de identidad

Gestiona:

\- solicitudes;

\- sesiones;

\- permisos;

\- relaciones;

\- auditoría.



\### 13.4 Integración con instituciones

Permite:

\- que una dependencia solicite atributos;

\- que la app responda con consentimiento;

\- que la dependencia reciba solo lo autorizado.



\---



\## 14. Modelo conceptual de datos



\### Entidades principales



\#### Persona

\- identificador único;

\- nombre;

\- CURP;

\- fecha de nacimiento;

\- tipo de persona.



\#### Perfil

\- perfil principal o dependiente;

\- método de acceso;

\- estado.



\#### Relación

\- tutor;

\- hijo;

\- cónyuge;

\- persona autorizada;

\- dependencia legal o voluntaria.



\#### Delegación

\- persona que autoriza;

\- persona autorizada;

\- alcance;

\- vigencia;

\- restricciones.



\#### Solicitud de atributos

\- institución;

\- trámite;

\- atributos requeridos;

\- finalidad.



\#### Consentimiento

\- aprobado o rechazado;

\- atributos autorizados;

\- vigencia.



\#### Evento de auditoría

\- usuario autenticado;

\- persona representada;

\- operación;

\- timestamp.



\---



\## 15. Matriz de compartición selectiva de datos



\### Regla general

No se comparten documentos completos por defecto.



Se comparten atributos puntuales según:

\- institución;

\- trámite;

\- persona objetivo;

\- marco de representación.



\### Ejemplos



\#### Educación

\*\*Trámite:\*\* inscripción escolar  

\*\*Datos permitidos:\*\*  

\- nombre del menor;  

\- CURP del menor;  

\- fecha de nacimiento;  

\- tutor responsable.



\#### Salud

\*\*Trámite:\*\* registro o cita médica  

\*\*Datos permitidos:\*\*  

\- nombre;  

\- CURP;  

\- parentesco o tutoría;  

\- contacto de emergencia.



\#### Programas sociales

\*\*Trámite:\*\* registro  

\*\*Datos permitidos:\*\*  

\- identidad;  

\- composición familiar cuando aplique;  

\- domicilio;  

\- datos específicos del programa.



\#### Financiero

\*\*Trámite:\*\* apertura de cuenta  

\*\*Datos permitidos:\*\*  

\- identidad del titular;  

\- mayoría de edad;  

\- domicilio;  

\- datos KYC definidos.



\---



\## 16. Diferenciadores de la propuesta



\### Frente a modelos tradicionales

\- no se limita a 1 persona por acceso;

\- no obliga a compartir todo;

\- no requiere compartir contraseñas;

\- no mezcla perfiles familiares;

\- no confunde identidad con representación.



\### Frente a soluciones aisladas

\- integra identidad, representación, consentimiento y trazabilidad;

\- permite uso familiar real;

\- mejora experiencia ciudadana;

\- fortalece seguridad y gobernanza.



\---



\## 17. Beneficios para gobierno



\### 17.1 Mejora en experiencia ciudadana

\- menos fricción en trámites;

\- atención a realidad familiar;

\- reducción de barreras digitales.



\### 17.2 Mayor seguridad

\- evita compartición de cuentas;

\- reduce uso indebido de credenciales;

\- fortalece autenticación.



\### 17.3 Mayor control y trazabilidad

\- claridad sobre quién actuó;

\- evidencia de representación;

\- registro de consentimiento.



\### 17.4 Mejor protección de datos

\- mínima divulgación;

\- finalidad explícita;

\- acceso contextual.



\### 17.5 Base para interoperabilidad

\- puede evolucionar hacia integración con múltiples dependencias;

\- habilita un ecosistema de trámites más ordenado.



\---



\## 18. Beneficios para ciudadanía



\- acceso más simple desde un solo dispositivo;

\- posibilidad de gestionar trámites familiares;

\- control sobre datos compartidos;

\- claridad sobre para qué se usan sus datos;

\- mayor confianza en el canal digital.



\---



\## 19. Riesgos a considerar



\### 19.1 Riesgo de confusión de contexto

Mitigación:

\- encabezado visible permanente con identidad y representación activa.



\### 19.2 Riesgo de acceso indebido en dispositivo compartido

Mitigación:

\- biometría;

\- PIN por perfil;

\- cierre automático de sesión.



\### 19.3 Riesgo de solicitud excesiva de datos por instituciones

Mitigación:

\- motor central de reglas;

\- matrices por trámite;

\- revisión de atributos permitidos.



\### 19.4 Riesgo de delegaciones mal administradas

Mitigación:

\- vigencias;

\- límites por trámite;

\- auditoría;

\- revocación.



\---



\## 20. Alcance del demo



Este demo no pretende resolver de inmediato todos los aspectos jurídicos o de infraestructura nacional.



Su propósito es demostrar de forma visual y operativa:



\- la lógica de perfiles familiares;

\- la mecánica de representación;

\- el flujo de consentimiento selectivo;

\- la trazabilidad de acciones;

\- la experiencia de usuario en un entorno tipo gobierno.



\---



\## 21. Roadmap sugerido



\### Fase 1. Piloto funcional

\- identidad individual;

\- perfiles múltiples en dispositivo;

\- representación tutor-menor;

\- consentimiento por trámite.



\### Fase 2. Integración institucional

\- conexión con 1 o 2 tipos de trámite prioritario;

\- reglas por dependencia;

\- historial auditable.



\### Fase 3. Expansión controlada

\- más relaciones;

\- más instituciones;

\- más atributos selectivos;

\- ecosistema interoperable.



\---



\## 22. Mensaje estratégico de cierre



La transformación digital del gobierno no solo requiere digitalizar trámites; requiere reconocer cómo viven realmente las personas.



Una identidad digital moderna debe permitir:

\- que una persona se autentique de forma segura;

\- que pueda actuar por sí misma o en representación válida de alguien más;

\- que comparta solo los datos necesarios;

\- y que todo ello ocurra con claridad, confianza y trazabilidad.



Esta propuesta plantea una evolución viable hacia una \*\*identidad digital familiar, contextual y centrada en la persona\*\*, apta para entornos gubernamentales con visión de interoperabilidad y protección de datos.



\---



\## 23. Frase final para presentación



> \*\*De una identidad individual aislada, a una identidad digital capaz de representar la realidad de las familias, los cuidados y los trámites cotidianos de la ciudadanía.\*\*



\---

