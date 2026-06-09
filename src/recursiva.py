ALFABETO_FITA = {"0", "1", "#", "X", "Y", "B"}

estados = {"q0", "q1", "q2", "q3", "q4", "q5", "q_aceita", "q_rejeita"}
estado_inicial = "q0"
estados_finais = {"q_aceita"}

def reconhecer(cadeia, mostrar_passos=False):
    fita = ["B"] + list(cadeia) + ["B"]
    cabecote = 1
    estado = estado_inicial
    passos = 0

    if "#" not in cadeia:
        print("Resultado: REJEITADA (Falta o caractere separador '#')")
        return False, estado

    if mostrar_passos:
        print(f"Estado inicial: {estado}")
        print(f"Fita inicial  : {''.join(fita)}")
        print(f"Cabeçote posicionado em: '{fita[cabecote]}'")

    while estado not in {"q_aceita", "q_rejeita"}:
        passos += 1
        simbolo_atual = fita[cabecote]
        estado_anterior = estado
        fita_antes = "".join(fita)

        
        if estado == "q0":
            if simbolo_atual == "0":
                fita[cabecote] = "X"
                cabecote += 1
                estado = "q1"
            elif simbolo_atual == "1":
                fita[cabecote] = "Y"
                cabecote += 1
                estado = "q2"
            elif simbolo_atual == "#":
                cabecote += 1
                estado = "q5"

        elif estado == "q1":
            if simbolo_atual in {"0", "1", "#", "X", "Y"}:

                if simbolo_atual == "0" and pasos_apos_hashtag(fita, cabecote):
                    fita[cabecote] = "X"
                    cabecote -= 1
                    estado = "q3"
                else:
                    cabecote += 1
            else:
                estado = "q_rejeita"

        elif estado == "q2":
            if simbolo_atual in {"0", "1", "#", "X", "Y"}:
                if simbolo_atual == "1" and pasos_apos_hashtag(fita, cabecote):
                    fita[cabecote] = "Y"
                    cabecote -= 1
                    estado = "q3"
                else:
                    cabecote += 1
            else:
                estado = "q_rejeita"

        elif estado == "q3":
            if simbolo_atual in {"0", "1", "#", "X", "Y"}:
                cabecote -= 1
            elif simbolo_atual == "B":
                cabecote += 1
                estado = "q4"

        elif estado == "q4":
            if simbolo_atual in {"X", "Y"}:
                cabecote += 1
            elif simbolo_atual in {"0", "1", "#"}:
                estado = "q0"

        elif estado == "q5":
            if simbolo_atual in {"X", "Y"}:
                cabecote += 1
            elif simbolo_atual == "B":
                estado = "q_aceita"
            else:
                estado = "q_rejeita"

        else:
            estado = "q_rejeita"

        if cabecote < 0 or cabecote >= len(fita):
            if mostrar_passos:
                print(f"Erro: Cabeçote saiu dos limites da fita!")
            estado = "q_rejeita"

        if mostrar_passos and estado_anterior != "q_rejeita":
            print(f"Passo {passos}: Estado {estado_anterior} -> {estado}")
            print(f"Fita : {fita_antes}")
            if cabecote >= len(fita):
                print("Lendo: Cabeçote saiu da fita")
            else:
                print(f"Lendo: '{fita[cabecote] if estado != 'q_aceita' else ' '}'")
            print("-" * 30)

    aceitou = estado in estados_finais

    if mostrar_passos:
        print(f"\nEstado final alcançado: {estado}")
        print(f"Fita final: {''.join(fita)}")
        print(f"Estado de aceitação: {aceitou}")

    return aceitou, passos

def pasos_apos_hashtag(fita, cabecote):
    idx_hashtag = fita.index("#")
    return cabecote > idx_hashtag

if __name__ == "__main__":
    cadeia = input("Digite um prompt com separador #: ")

    aceitou, passos = reconhecer(cadeia, mostrar_passos=True)

    print("\n" + "=" * 40)

    if aceitou:
        print("Resultado: ACEITA")
    else:
        print("Resultado: REJEITADA")

    print(f"Passos executados: {passos}")