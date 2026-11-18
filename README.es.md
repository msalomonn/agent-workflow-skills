# Agent Workflow Skills

**Skills reutilizables para agentes de programación: definir el trabajo, retomarlo con contexto y verificar lo entregado.**

[English](README.md) · [Instalación](docs/installation.md) · [Demo local](examples/cart/README.md) · [Validación](docs/validation.md)

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

| Skill | Uso |
| --- | --- |
| `workflow-spec` | Comportamiento y criterios de aceptación. |
| `workflow-plan` | Plan con resultados verificables. |
| `workflow-execute` | Implementación y continuidad. |
| `workflow-debug` | Diagnóstico y corrección de fallos. |
| `workflow-audit` | Revisión técnica del cambio. |
| `workflow-verify` | Evidencia antes de declarar una entrega. |
| `workflow-doctor` | Diagnóstico del entorno y accesos. |
| `workflow-triage` | Clasificación de pedidos y siguiente acción. |
| `workflow-research` | Investigación técnica con fuentes. |
| `workflow-github-status` | Estado de issues, PRs y bloqueos. |
| `workflow-handoff` | Guardar y retomar un checkpoint. |
| `workflow-release` | Preparar o publicar una versión según las reglas del repo. |

No es obligatorio recorrerlas todas. Un bug puede empezar por debugging; una tarea clara no necesita repetir la especificación. Las convenciones, herramientas y autorizaciones las aporta cada proyecto.

## Probar y contribuir

La [demo del carrito](examples/cart/README.md) propone un bug reproducible para practicar debugging, verificación y reanudación sin cuentas externas. Para comprobar el paquete:

```sh
python3 scripts/check_repository.py
```

La versión 0.1.0 incluye pruebas del exportador y escenarios para evaluar el comportamiento de las skills. No promete compatibilidad universal ni una mejora de productividad medida. Consultá los [límites de validación](docs/validation.md) y la [guía de contribución](CONTRIBUTING.md).

Creado por [Manuel Salomon](https://github.com/msalomonn). Podés usarlo, modificarlo y compartirlo bajo [licencia MIT](LICENSE).
