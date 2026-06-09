
DIGITOS = set("0123456789")

estados = {f"q{i}" for i in range(15)}

estado_inicial = "q0"
estados_finais = {"q14"}
transicoes = {}

for d in DIGITOS:
    transicoes[("q0", d)] = "q1"
    transicoes[("q1", d)] = "q2"
    transicoes[("q2", d)] = "q3"

transicoes[("q3", ".")] = "q4"

for d in DIGITOS:
    transicoes[("q4", d)] = "q5"
    transicoes[("q5", d)] = "q6"
    transicoes[("q6", d)] = "q7"

transicoes[("q7", ".")] = "q8"

for d in DIGITOS:
    transicoes[("q8", d)] = "q9"
    transicoes[("q9", d)] = "q10"
    transicoes[("q10", d)] = "q11"

transicoes[("q11", "-")] = "q12"

for d in DIGITOS:
    transicoes[("q12", d)] = "q13"
    transicoes[("q13", d)] = "q14"

def reconhecer(cadeia, mostrar_passos=False):
    estado = estado_inicial
    passos = 0

    if mostrar_passos:
        print(f"Estado inicial: {estado}")
        print()

    for simbolo in cadeia:
        chave = (estado, simbolo)
        if chave not in transicoes:
            if mostrar_passos:
                print(f"Não existe transição para ({estado}, '{simbolo}')")
            return False, passos

        proximo_estado = transicoes[chave]
        passos += 1

        if mostrar_passos:
            print(f"Passo {passos}: {estado} -- {simbolo} --> {proximo_estado}")

        estado = proximo_estado

    aceitou = estado in estados_finais

    if mostrar_passos:
        print(f"Estado final alcançado: {estado}")
        print(f"Estado de aceitação: {aceitou}")

    return aceitou, passos

if __name__ == "__main__":

    cadeia = input("Digite um cpf: ")
    
    aceitou, passos = reconhecer(cadeia, mostrar_passos=True)

    print("\n" + "=" * 40)

    if aceitou:
        print("Resultado: ACEITA")
    else:
        print("Resultado: REJEITADA")

    print(f"Passos executados: {passos}")