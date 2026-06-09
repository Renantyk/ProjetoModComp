
LETRAS_OPERADORES = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/")
ABRE_PAR = "("
FECHA_PAR = ")"

estados = {"q0", "q1", "q2"}
estado_inicial = "q0"
estados_finais = {"q2"}

# Símbolo especial para marcar o fundo da pilha (padrão na definição formal de PDAs)
FONDO_PILHA = "$"

def reconhecer(cadeia, mostrar_passos=False):
    estado = estado_inicial
    passos = 0
    
    pilha = [FONDO_PILHA]

    if mostrar_passos:
        print(f"Estado inicial: {estado}")
        print(f"Pilha inicial : {pilha}")
        print()

    estado = "q1"
    passos += 1
    if mostrar_passos:
        print(f"Passo {passos}: Transição inicial q0 -> q1 (Pilha pronta)")

    for simbolo in cadeia:
        passos += 1
        topo = pilha[-1] if pilha else None

        if simbolo == ABRE_PAR:
            pilha.append(ABRE_PAR)
            if mostrar_passos:
                print(f"Passo {passos}: {estado} -- '{simbolo}' --> {estado} | Empilhou '{ABRE_PAR}' (Pilha: {pilha})")

        elif simbolo == FECHA_PAR:
            if topo == ABRE_PAR:
                pilha.pop()
                if mostrar_passos:
                    print(f"Passo {passos}: {estado} -- '{simbolo}' --> {estado} | Desempilhou '{ABRE_PAR}' (Pilha: {pilha})")
            else:
                if mostrar_passos:
                    print(f"Erro no Passo {passos}: Tentativa de fechar parênteses sem abertura correspondente.")
                return False, passos

        elif simbolo in LETRAS_OPERADORES:
            if mostrar_passos:
                print(f"Passo {passos}: {estado} -- '{simbolo}' --> {estado} | Ignorou pilha (Pilha: {pilha})")

        else:
            if mostrar_passos:
                print(f"Erro no Passo {passos}: Símbolo inválido '{simbolo}' detectado.")
            return False, passos

    if pilha == [FONDO_PILHA]:
        estado = "q2"
        passos += 1
        if mostrar_passos:
            print(f"Passo {passos}: Cadeia consumida com sucesso. Transição q1 -> q2 (Pilha limpa)")
    else:
        if mostrar_passos:
            print(f"Erro final: Sobraram parênteses abertos na pilha: {pilha}")

    aceitou = estado in estados_finais

    if mostrar_passos:
        print(f"\nEstado final alcançado: {estado}")
        print(f"Pilha final: {pilha}")
        print(f"Estado de aceitação: {aceitou}")

    return aceitou, passos

if __name__ == "__main__":
    cadeia = input("Digite um texto que abra e feche parenteses: ")

    aceitou, passos = reconhecer(cadeia, mostrar_passos=True)

    print("\n" + "=" * 40)

    if aceitou:
        print("Resultado: ACEITA")
    else:
        print("Resultado: REJEITADA")

    print(f"Passos executados: {passos}")