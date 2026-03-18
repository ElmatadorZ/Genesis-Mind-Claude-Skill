from matador.matador_core import MatadorCore

if __name__ == "__main__":
    core = MatadorCore()

    result = core.run("Bitcoin drops due to macro uncertainty")

    print("\n=== GENESIS OUTPUT ===\n")
    for k, v in result.items():
        print(f"{k}: {v}")
