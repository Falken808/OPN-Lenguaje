# OPN BluePanda

OPN BluePanda is a Python-backed language with a simple C/JS-like syntax and a stable CLI command: `opn`.

ES (optional): OPN BluePanda es un lenguaje sobre Python, con sintaxis simple y comando estable `opn`.

## Version
- Current version: `0.1.2`
- CLI command: `opn`
- Runtime: OPN transpiles to Python, then executes on Python.

## What is new in 0.1.2
- Automatic project `.venv` management.
- Just-in-time dependency install when `ModuleNotFoundError` appears.
- Dependency tracking in `opn.json`.
- Python module proxy via `opn -m ...`.
- Portable binary build via `opn build ...`.

## Quick commands
```bash
opn app.opn
opn run app.opn
opn compile app.opn -o app.py
opn -m pip install requests
opn build app.opn -o dist/app
```

## Documentation map
- Quickstart: `docs/quickstart.md`
- Syntax: `docs/syntax.md`
- CLI and Build: `docs/compiler_cli.md`
- Performance: `docs/performance.md`
- AI Prompt Template: `docs/ia_formulario.md`

## Typical workflow
1. Create `app.opn`.
2. Run with `opn app.opn`.
3. Let OPN install missing dependencies when needed.
4. Review dependencies in `opn.json`.
5. Build a portable binary with `opn build app.opn`.

## Project metadata (`opn.json`)
```json
{
  "name": "my-project",
  "version": "0.1.2",
  "dependencies": ["pygame", "requests"]
}
```

## Web docs
- Root entry: `index.html`
- Full web portal: `docs/html/index.html`

## License
MIT
