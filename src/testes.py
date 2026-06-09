from regular import reconhecer as lr_reconhecer
from recursiva import reconhecer as r_reconhecer
from livre_contexto import reconhecer as llc_reconhecer
import sys

if len(sys.argv) > 1:
    if sys.argv[1] != "executar":
        sys.exit(0)
    
    with open("testes/testes_regular.txt", "r") as testes:
        for t in testes:
            t = t.strip()
            aceitou, passos = lr_reconhecer(t, True)

            print("\n" + "=" * 40)

            print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

            print(f"Passos executados: {passos}")

            input("Aperte enter para continuar...")
    
    with open("testes/testes_livre_contexto.txt", "r") as testes:
        for t in testes:
            t = t.strip()
            aceitou, passos = llc_reconhecer(t, True)

            print("\n" + "=" * 40)

            print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

            print(f"Passos executados: {passos}")

            input("Aperte enter para continuar...")
    

    with open("testes/testes_recursiva.txt", "r") as testes:
        for t in testes:
            t = t.strip()
            aceitou, passos = r_reconhecer(t, True)

            print("\n" + "=" * 40)

            print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

            print(f"Passos executados: {passos}")

            input("Aperte enter para continuar...")
        
    sys.exit(0)

mostrar_passos = True
escolha = 0

while True:
    print("[1] Testar LR")
    print("[2] Testar LLC")
    print("[3] Testar R")
    print(f"[4] {'Não mostrar' if mostrar_passos else 'Mostrar'} passos")
    escolha = int(input("Escolha uma das opções acima: "))

    match escolha:
        case 1:
            with open("testes/testes_regular.txt", "r") as testes:
                for t in testes:
                    t = t.strip()
                    aceitou, passos = lr_reconhecer(t, mostrar_passos)

                    print("\n" + "=" * 40)

                    print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

                    print(f"Passos executados: {passos}")

                    input("Aperte enter para continuar...")
        case 2:
            with open("testes/testes_livre_contexto.txt", "r") as testes:
                for t in testes:
                    t = t.strip()
                    aceitou, passos = llc_reconhecer(t, mostrar_passos)

                    print("\n" + "=" * 40)

                    print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

                    print(f"Passos executados: {passos}")

                    input("Aperte enter para continuar...")
        case 3:
            with open("testes/testes_recursiva.txt", "r") as testes:
                for t in testes:
                    t = t.strip()
                    aceitou, passos = r_reconhecer(t, mostrar_passos)

                    print("\n" + "=" * 40)

                    print(f"Resultado de {t}: {'ACEITA' if aceitou else 'REJEITADA'}")

                    print(f"Passos executados: {passos}")

                    input("Aperte enter para continuar...")
        case 4:
            mostrar_passos = not mostrar_passos
    
