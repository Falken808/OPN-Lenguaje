# Quickstart - OPN BluePanda

[Back to README](../README.md)

This guide gets you from zero to a working project in minutes.

ES (optional): Esta guia te lleva de cero a un proyecto funcionando en minutos.

## Requirements
- Python 3.10+
- `opn` command available (or `python src/opn.py` fallback)

## 1. Create your first file
Create `hello.opn`:

```opn
var greeting = "Hello BluePanda";
print(greeting);
```

Run:

```bash
opn hello.opn
```

## 2. Compile to Python

```bash
opn compile hello.opn -o hello.py
python hello.py
```

## 3. Install dependencies in project venv

```bash
opn -m pip install pygame
```

If a module is missing during execution, OPN can auto-install it and update `opn.json`.

## 4. Build a portable binary

```bash
opn build hello.opn -o dist/hello
```

Output:
- Windows: `dist/hello.exe`
- Linux/macOS: `dist/hello`

## 5. Continue learning
- Syntax reference: `docs/syntax.md`
- CLI details: `docs/compiler_cli.md`
- Performance checklist: `docs/performance.md`
- AI workflow template: `docs/ia_formulario.md`
