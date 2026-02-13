# Syntax Reference - OPN BluePanda

[Back to README](../README.md)

Authoritative syntax guide for version `0.1.2`.

ES (optional): Guia de sintaxis oficial para la version `0.1.2`.

## Language rules
- Statements end with `;`.
- Blocks use `{ ... }`.
- Comments use `//`.

## Supported keywords
- `var`, `function`, `func`, `class`
- `if`, `else`, `while`, `for`, `return`
- `true`, `false`, `null`, `this`
- `import`, `from`, `as`

## Variables and literals
```opn
var name = "Ana";
var age = 25;
var active = true;
var list = [1, 2, 3];
var map = {"name": "Ana", "age": 25};
```

## Operators
- Arithmetic: `+ - * / %`
- Comparison: `== != < <= > >=`
- Logical: `&& || !`

## Control flow
```opn
if (age >= 18) {
    print("Adult");
} else {
    print("Minor");
}

for (var i = 0; i < 3; i = i + 1) {
    print(i);
}

while (age > 0) {
    age = age - 1;
}
```

## Functions and classes
```opn
function sum(a, b) {
    return a + b;
}

class Person {
    function init(name) {
        this.name = name;
    }
}
```

## Imports
```opn
import pygame;
from math import sqrt;
from math import floor as floor_int;
```

## Known non-goals in current parser
- `do...while`
- `try/catch`
- Additional JS-only grammar extensions

## Related guides
- Quickstart: `docs/quickstart.md`
- CLI and build: `docs/compiler_cli.md`
- Performance: `docs/performance.md`
