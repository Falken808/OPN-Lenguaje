import argparse
import sys
import traceback

from opn2 import (
    OPNError,
    OPNInterpreter,
    build_opn_binary,
    compile_opn_file,
    print_opn_error,
    run_module_in_venv,
)


def main(argv: list[str]) -> int:
    if len(argv) >= 1 and argv[0] == "-m":
        return run_module_in_venv(argv[1:])

    parser = argparse.ArgumentParser(
        prog="opn",
        description="CLI de OPN BluePanda: ejecutar, compilar o empaquetar .opn",
    )
    parser.add_argument(
        "args",
        nargs="+",
        help="Uso: opn archivo.opn | opn run archivo.opn | opn compile in.opn -o out.py | opn build app.opn -o dist/app",
    )
    parser.add_argument("-o", "--output", help="Ruta de salida para compile/build")
    ns = parser.parse_args(argv)

    if len(ns.args) == 1 and ns.args[0].endswith(".opn"):
        path = ns.args[0]
        try:
            with open(path, "r", encoding="utf-8") as f:
                OPNInterpreter().run(f.read(), source_name=path, source_path=path)
        except FileNotFoundError as err:
            raise OPNError(
                "No se encontro el archivo .opn",
                code="OPN4001",
                phase="CLI",
                source_name=path,
                hint="Verifica la ruta o el nombre del archivo.",
                details=str(err),
            ) from err
        return 0

    cmd = ns.args[0]
    if cmd == "run":
        if len(ns.args) < 2:
            raise OPNError(
                "Falta archivo .opn para run",
                code="OPN4002",
                phase="CLI",
                hint="Uso: opn run archivo.opn",
            )
        path = ns.args[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                OPNInterpreter().run(f.read(), source_name=path, source_path=path)
        except FileNotFoundError as err:
            raise OPNError(
                "No se encontro el archivo .opn",
                code="OPN4001",
                phase="CLI",
                source_name=path,
                hint="Verifica la ruta o el nombre del archivo.",
                details=str(err),
            ) from err
        return 0

    if cmd == "compile":
        if len(ns.args) < 2:
            raise OPNError(
                "Falta archivo .opn para compile",
                code="OPN4003",
                phase="CLI",
                hint="Uso: opn compile in.opn -o out.py",
            )
        src = ns.args[1]
        out = ns.output or src.replace(".opn", ".py")
        if out == src:
            out = src + ".py"
        try:
            compile_opn_file(src, out)
        except FileNotFoundError as err:
            raise OPNError(
                "No se encontro el archivo fuente para compilar",
                code="OPN4001",
                phase="CLI",
                source_name=src,
                hint="Verifica la ruta de entrada.",
                details=str(err),
            ) from err
        print(f"Compilado: {src} -> {out}")
        return 0

    if cmd == "build":
        if len(ns.args) < 2:
            raise OPNError(
                "Falta archivo .opn para build",
                code="OPN4009",
                phase="Build",
                hint="Uso: opn build app.opn -o dist/app",
            )
        src = ns.args[1]
        try:
            out = build_opn_binary(src, ns.output)
        except FileNotFoundError as err:
            raise OPNError(
                "No se encontro el archivo fuente para build",
                code="OPN4001",
                phase="Build",
                source_name=src,
                hint="Verifica la ruta de entrada.",
                details=str(err),
            ) from err
        print(f"Binario generado: {out}")
        return 0

    raise OPNError(
        f"Comando no soportado: {cmd}",
        code="OPN4004",
        phase="CLI",
        hint="Comandos validos: run, compile, build o -m",
    )


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except OPNError as exc:
        print_opn_error(exc)
        raise SystemExit(1)
    except Exception as exc:
        err = OPNError(
            "Fallo interno no controlado",
            code="OPN9000",
            phase="Interno",
            details="".join(traceback.format_exception_only(type(exc), exc)).strip(),
        )
        print_opn_error(err)
        raise SystemExit(1)
