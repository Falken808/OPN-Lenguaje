# Performance Guide - OPN BluePanda

[Back to README](../README.md)

Practical performance rules and profiling workflow.

ES (optional): Reglas practicas de rendimiento y flujo de perfilado.

## Built-in runtime behavior
- LRU cache for transpile/compile stages.
- Interpreter reuse across repeated runs.
- Final execution on Python runtime.

## Performance habits
- Cache repeated values in loops.
- Prefer dictionary lookups for key-based access.
- Avoid heavy string concatenation in tight loops.
- Profile first, optimize second.

## Example pattern
Better:

```opn
var n = items.length;
for (var i = 0; i < n; i = i + 1) {
    print(items[i]);
}
```

## Production check
```bash
opn compile app.opn -o app.py
python -m cProfile -s cumtime app.py
opn build app.opn -o dist/app
```

## Measurement workflow
1. Define a test case.
2. Measure baseline.
3. Change one thing.
4. Measure again.
5. Keep only proven improvements.

## Related guides
- Syntax: `docs/syntax.md`
- CLI and build: `docs/compiler_cli.md`
- AI workflow: `docs/ia_formulario.md`
