# Agent Workflow Skills

**Skills reutilizables para agentes de programación: definir el trabajo, retomarlo con contexto y verificar lo entregado.**

[English](README.md) · [Descargar v0.1.1](https://github.com/msalomonn/agent-workflow-skills/releases/tag/v0.1.1) · [Instalación](docs/installation.md) · [Ejemplos de uso](#ejemplos-de-uso) · [Demo local](examples/cart/README.md) · [Validación](docs/validation.md)

Un conjunto de 12 skills para desarrollo de software. Cada carpeta exportada incluye sus instrucciones, referencias y plantillas. Podés instalar las que necesites y combinarlas con el proceso de tu proyecto.

El objetivo es conectar alcance, estado real del repositorio y evidencia. Un cambio implementado, un PR mergeado y una entrega en producción tienen comprobaciones diferentes. Los checkpoints permiten retomar sin depender exclusivamente de una conversación anterior.

## Primer uso

Necesitás Git, Python 3.9+ para exportar y un agente que admita carpetas `SKILL.md`. El exportador usa únicamente la biblioteca estándar y no realiza solicitudes de red.

```sh
git clone https://github.com/msalomonn/agent-workflow-skills.git
cd agent-workflow-skills
python3 scripts/export_skills.py --output dist/inicio \
  --skill workflow-debug --skill workflow-verify --skill workflow-handoff
python3 scripts/export_skills.py --verify dist/inicio
```

Copiá las carpetas completas exportadas al directorio de skills del proyecto. En Codex se usa `.agents/skills/`. Revisá primero si ya existen carpetas con esos nombres para conservar tus personalizaciones. La [guía completa](docs/installation.md) explica instalación y actualización.

Ejemplo de pedido:

```text
Usá workflow-debug para reproducir y corregir el error en el total.
Limitá el cambio al bug y registrá la verificación antes y después.
```

Las instrucciones están escritas en inglés, pero podés usarlas con pedidos en español. El idioma de respuesta depende del contexto y del agente.

## Qué incluye

| Skill | Uso | Ejemplo |
| --- | --- | --- |
| [workflow-spec](skills/workflow-spec/SKILL.md) | Comportamiento y criterios de aceptación. | [Ver ejemplo](#workflow-spec) |
| [workflow-plan](skills/workflow-plan/SKILL.md) | Plan con resultados verificables. | [Ver ejemplo](#workflow-plan) |
| [workflow-execute](skills/workflow-execute/SKILL.md) | Implementación y continuidad. | [Ver ejemplo](#workflow-execute) |
| [workflow-debug](skills/workflow-debug/SKILL.md) | Diagnóstico y corrección de fallos. | [Ver ejemplo](#workflow-debug) |
| [workflow-audit](skills/workflow-audit/SKILL.md) | Revisión técnica del cambio. | [Ver ejemplo](#workflow-audit) |
| [workflow-verify](skills/workflow-verify/SKILL.md) | Evidencia antes de declarar una entrega. | [Ver ejemplo](#workflow-verify) |
| [workflow-doctor](skills/workflow-doctor/SKILL.md) | Diagnóstico del entorno y accesos. | [Ver ejemplo](#workflow-doctor) |
| [workflow-triage](skills/workflow-triage/SKILL.md) | Clasificación de pedidos y siguiente acción. | [Ver ejemplo](#workflow-triage) |
| [workflow-research](skills/workflow-research/SKILL.md) | Investigación técnica con fuentes. | [Ver ejemplo](#workflow-research) |
| [workflow-github-status](skills/workflow-github-status/SKILL.md) | Estado de issues, PRs y bloqueos. | [Ver ejemplo](#workflow-github-status) |
| [workflow-handoff](skills/workflow-handoff/SKILL.md) | Guardar y retomar un checkpoint. | [Ver ejemplo](#workflow-handoff) |
| [workflow-release](skills/workflow-release/SKILL.md) | Preparar o publicar una versión según las reglas del repo. | [Ver ejemplo](#workflow-release) |

No es obligatorio recorrerlas todas. Un bug puede empezar por debugging; una tarea clara no necesita repetir la especificación. Las convenciones, herramientas y autorizaciones las aporta cada proyecto.

## Ejemplos de uso

Instalá cada skill antes de usar su ejemplo: el comando inicial de arriba instala únicamente debug, verify y handoff. La [guía de instalación](docs/installation.md) explica cómo exportar todas o una selección. Copiá los pedidos en tu agente y reemplazá los nombres ilustrativos de archivos, versiones y repositorios por los de tu proyecto.

Un pedido útil indica el resultado buscado, los archivos o issue relevantes, las restricciones y si querés análisis o implementación. Sumá los tests, logs o criterios de aceptación disponibles. Los resultados esperados describen el entregable; su detalle depende de la tarea y las herramientas disponibles.

### workflow-spec

Usala cuando necesitás definir mejor el comportamiento antes de implementar. Aportá el funcionamiento actual, la necesidad del usuario, las restricciones y cualquier especificación existente. Revisa la implementación para evitar proponer trabajo ya resuelto.

```text
Usá workflow-spec para definir reintentos de importaciones CSV fallidas.
Revisá importer.py y los requisitos existentes. Una importación fallida
puede dejar filas guardadas; todavía no decidimos si omitirlas o reemplazarlas
al reintentar. Definí criterios de aceptación y casos de error, e identificá
esa decisión pendiente. Escribí la propuesta en docs/import-retries.md,
sin implementar todavía.
```

**Resultado esperado:** comportamiento observable, criterios comprobables, exclusiones, dependencias y decisiones pendientes. Si una decisión bloquea solo parte del trabajo, deja claro qué parte.

### workflow-plan

Usala para convertir un alcance acordado en pasos de implementación o actualizar un plan existente. Aportá los criterios de aceptación y el plan actual, si lo hay. Comprueba el avance real antes de agregar tareas.

```text
Usá workflow-plan con docs/import-retries.md y docs/plan.md.
El lector CSV podría estar implementado: comprobalo en el repositorio.
Planificá lo que falta con IDs de pasos, dependencias, interfaces afectadas
y una comprobación para cada resultado. Mantené explícitas las decisiones
pendientes sobre reintentos. Actualizá docs/plan.md sin implementar.
```

**Resultado esperado:** un plan breve que conserva lo completado, cubre los criterios de aceptación, identifica pasos condicionados y señala la próxima acción ejecutable.

### workflow-execute

Usala cuando el cambio está claro y autorizaste su implementación. Aportá el alcance acordado, el plan o checkpoint relevante y el comando de verificación si lo conocés. Contrasta esos documentos con el código actual y conserva cambios ajenos a la tarea.

```text
Usá workflow-execute para implementar el límite de tamaño acordado en
docs/import-retries.md. Revisá docs/plan.md y continuá el paso pendiente.
Conservá mis cambios de interfaz que no pertenecen a esta tarea.
Agregá tests para los límites y ejecutá las pruebas del importador.
Dejá el cambio local y actualizá el checkpoint.
```

**Resultado esperado:** implementación dentro del alcance, resultados de verificación asociados al cambio actual y un checkpoint con lo completado y pendiente. Prepara un PR solo cuando compartirlo forma parte del pedido.

### workflow-debug

Usala para un bug reproducible o una falla intermitente con evidencia disponible. Aportá resultado esperado y real, entrada que dispara el error, entorno y logs o tests. Indicá si querés solo diagnóstico o también una corrección.

Para este ejemplo, prepará el proyecto descartable de la [demo del carrito](examples/cart/README.md), instalá la skill allí y abrí tu agente en ese proyecto.

```text
Usá workflow-debug en este proyecto del carrito. Las cantidades mayores a uno producen
un total incorrecto y un ítem con cantidad cero no debe sumar al total.
Reproducí el error ejecutando python3 -B -m unittest -v desde la raíz del proyecto,
identificá la causa y corregila. Conservá el contrato de entrada existente
y verificá todos los casos.
```

**Resultado esperado:** reproducción, evidencia de la causa, corrección autorizada y resultados antes y después. Si la causa sigue sin resolverse, indica la incertidumbre y qué observación falta.

### workflow-audit

Usala para revisar un diff o PR y encontrar defectos concretos. Aportá revisión base y objetivo o enlace al PR, comportamiento esperado y criterios de aceptación. El diff completo y su contexto permiten una revisión más amplia que un fragmento aislado.

```text
Usá workflow-audit para revisar la rama actual contra origin/main.
El cambio debe aplicar descuentos porcentuales usando centavos enteros.
Revisá redondeos y valores límite, y reproducí las posibles regresiones.
Informá cada hallazgo con archivo, línea, condición que lo dispara,
impacto y evidencia. Solo revisá: no edites código ni publiques comentarios.
```

**Resultado esperado:** hallazgos confirmados ordenados por impacto, revisión examinada y límites de cobertura. Distingue preferencias de estilo de defectos; no encontrar errores no equivale a una aprobación formal ni garantiza su ausencia.

### workflow-verify

Usala antes de declarar terminado un trabajo. Aportá criterios de aceptación, revisión objetivo y evidencia disponible de tests, revisión o despliegue. Comprueba si esa evidencia sigue vigente y ejecuta los controles faltantes dentro del alcance.

```text
Usá workflow-verify para evaluar el cambio del importador contra
docs/import-retries.md. Comprobá si los tests registrados cubren el HEAD
actual y ejecutá las verificaciones locales que falten.
El PR está mergeado, pero todavía no se inspeccionó producción.
Indicá qué está verificado, qué falló y qué sigue pendiente.
No despliegues ni cierres el issue.
```

**Resultado esperado:** tabla de criterios, evidencia y resultados, con fallos o faltantes explícitos y próxima acción. Implementación, merge, despliegue y aceptación se evalúan por separado.

### workflow-doctor

Usala al preparar un entorno o cuando la configuración, las herramientas o los accesos bloquean una tarea. Indicá qué querés hacer y el mensaje de error, si existe. Revisa únicamente las capacidades necesarias para esa tarea.

```text
Usá workflow-doctor para comprobar si este repositorio está listo para
desarrollo local en Python. Revisá instrucciones del repo, runtime,
comandos documentados de tests y recursos de las skills instaladas.
El acceso a GitHub es opcional para esta tarea. Diagnosticá sin cambiar
configuración e indicá la solución mínima para cada bloqueo.
```

**Resultado esperado:** comprobaciones clasificadas como listas, fallidas, desconocidas o no aplicables, con evidencia y soluciones. Distingue herramientas ausentes, destino incorrecto, autenticación y problemas de red sin exponer credenciales.

### workflow-triage

Usala para organizar pedidos o un backlog antes de empezar a trabajar. Aportá los pedidos, issues existentes e impacto conocido. Busca duplicados y propone la siguiente acción sin inventar urgencia ni responsables.

```text
Usá workflow-triage sobre requests.md y los issues de backlog.json.
Dos pedidos solicitan reintentar importaciones fallidas; otro pide mostrar
el progreso. Identificá posibles duplicados, contexto faltante y próxima
acción para cada uno. Devolvé una tabla con evidencia y prioridad sugerida.
No crees ni cierres tickets, no asignes personas y no implementes todavía.
```

**Resultado esperado:** tabla compacta de pedidos, clasificación, evidencia, prioridades sugeridas, elementos relacionados y próximas acciones. Aclara cuando falta información sobre impacto o no se pudo consultar toda la cola.

### workflow-research

Usala cuando una decisión técnica necesita evidencia. Aportá la decisión, restricciones de runtime o dependencias y la implementación actual. Compara opciones viables con fuentes primarias y experimentos acotados cuando aportan información.

```text
Usá workflow-research para elegir cómo parsear CSV en este proyecto.
Necesitamos Python 3.9+, comas y saltos de línea entre comillas, y ninguna
dependencia externa en runtime. Revisá el lector actual y comparalo con
la propuesta de separar líneas por comas. Consultá documentación oficial
de la versión relevante y ejecutá un experimento pequeño.
Recomendá una opción sin cambiar la aplicación ni instalar dependencias.
```

**Resultado esperado:** recomendación, alternativas, fuentes enlazadas, hechos separados de inferencias y el experimento mínimo pendiente. La investigación no inicia automáticamente la implementación.

### workflow-github-status

Usala para conocer el estado de issues, PRs, checks y bloqueos de un repositorio concreto. Indicá el repositorio exacto y el alcance o período. Consultar el estado en vivo requiere un conector o CLI de GitHub con acceso de lectura; una captura de datos permite un informe limitado.

```text
Usá workflow-github-status para owner/repository, enfocándote en issues
abiertos y PRs mergeados durante los últimos siete días. Revisá checks
vinculados y criterios de aceptación pendientes. Separá código mergeado,
despliegue y entrega verificada. Incluí enlaces, momento de observación,
bloqueos y próximas acciones. Solo lectura: no actualices issues ni envíes
un resumen al equipo.
```

**Resultado esperado:** resumen que separa resultados completados, trabajo en curso, dependencias y desconocidos. Comprueba si los checks verdes cubren la revisión actual y explicita límites de acceso o paginación.

### workflow-handoff

Usala para guardar el avance o retomar una tarea autorizada en una sesión nueva. Para guardar, aportá la tarea y sus artefactos; para retomar, el checkpoint. El checkpoint conserva evidencia y el estado actual del repo determina qué falta.

```text
Usá workflow-handoff para guardar esta tarea en docs/checkpoint.md.
Registrá HEAD, cambios sin commit, decisiones, verificaciones completadas,
trabajo pendiente y primera acción siguiente. Usá rutas de artefactos
relativas al repositorio.
```

En otra sesión:

```text
Usá workflow-handoff para retomar docs/checkpoint.md y terminar el arreglo
local. Primero contrastalo con la rama y los archivos actuales: otra persona
podría haber completado parte del trabajo. Conservá cambios ajenos y repetí
solo las verificaciones invalidadas por cambios o todavía pendientes.
```

**Resultado esperado:** un checkpoint recuperable, o una nota de reconciliación seguida del próximo paso pendiente autorizado. Guardar contexto no lo envía a nadie ni autoriza por sí solo una implementación futura.

### workflow-release

Usala para preparar una versión o publicarla cuando lo pedís explícitamente. Aportá la versión o resultado buscado, revisión objetivo y política de releases del proyecto. Distingue preparación, borrador, publicación y despliegue.

```text
Usá workflow-release para preparar la próxima versión patch desde el HEAD
actual. Revisá la política de versionado y la release anterior.
Actualizá versión y changelog, comprobá tests y revisiones contra el commit
objetivo, y prepará notas con indicaciones de recuperación.
No crees un tag remoto, no publiques la release ni despliegues.
```

**Resultado esperado:** versión y notas consistentes, commit objetivo, verificaciones y condiciones pendientes para publicar. Cuando también se solicita publicación, comprueba primero tags y releases existentes y después verifica destino y artefactos publicados.

## Combinar skills según el resultado

| Situación | Secuencia útil | Qué aporta cada paso |
| --- | --- | --- |
| Una funcionalidad ambigua | spec → plan → execute → audit → verify | Comportamiento acordado, pasos concretos, implementación, revisión de defectos y evidencia de aceptación. |
| Un cálculo incorrecto | debug → verify | Reproducción y corrección, luego comprobación contra todos los criterios de aceptación. |
| Una tarea interrumpida | handoff → execute → verify | Contexto reconciliado, solo la implementación pendiente y evidencia actual. |
| Una versión candidata | audit → verify → release | Hallazgos, preparación comprobada para esa revisión y preparación de release o publicación autorizada. |

Usá únicamente los pasos necesarios. Las decisiones y los tests todavía vigentes se conservan; nombrar una secuencia no autoriza por sí solo publicar o desplegar.

## Probar y contribuir

La [demo del carrito](examples/cart/README.md) propone un bug reproducible para practicar debugging, verificación y reanudación sin cuentas externas. Para comprobar el paquete:

```sh
python3 scripts/check_repository.py
```

La versión 0.1.1 incluye 21 pruebas del paquete, cuatro sesiones independientes que ejercitaron las 12 skills y una comprobación de detección nativa en Codex. No promete compatibilidad universal ni una mejora de productividad medida. Consultá los [límites de validación](docs/validation.md) y la [guía de contribución](CONTRIBUTING.md).

Creado por [Manuel Salomon](https://github.com/msalomonn). Podés usarlo, modificarlo y compartirlo bajo [licencia MIT](LICENSE).
