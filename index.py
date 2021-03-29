def display():
    mensagem_inicializacao()

    print("Operações: (1) Soma | (2) Subtração | (3) Multiplicação | (4) Divisão")

    operacao = leia_operacao()
    primeiro_numero = leia_numero(1)
    segundo_numero = leia_numero(2)

    seleciona_operacao(operacao, primeiro_numero, segundo_numero)

def mensagem_inicializacao():
    print("#########################################################")
    print("###################### CALCULADORA ######################")
    print("#########################################################\n")

def leia_operacao():
    while True:
        entrada = input("\nDigite uma operação: ")

        if (entrada.isnumeric()):
            entrada = int(entrada)

            if (entrada > 0 and entrada < 5):
                break
            else:
                print("ERRO! Digite uma operação válida!")
        else:
            print("ERRO! Digite uma operação válida!")

    return entrada

def leia_numero(numero):
    while True:
        if (numero == 1):
            entrada = input("\nDigite o primeiro número: ")
        else:
            entrada = input("\nDigite o segundo número: ")

        try:
            entrada = float(entrada)
            break
        except ValueError:
            print("ERRO! Digite um número válido!")

    return entrada

def seleciona_operacao(operacao, primeiro_numero, segundo_numero):
    if (operacao == 1):
        resultado = somar(primeiro_numero, segundo_numero)
        print(f"\nResultado de {primeiro_numero:.2f} + {segundo_numero:.2f} = {resultado:.2f}")
    elif (operacao == 2):
        resultado = subtrair(primeiro_numero, segundo_numero)
        print(f"\nResultado de {primeiro_numero:.2f} - {segundo_numero:.2f} = {resultado:.2f}")
    elif (operacao == 3):
        resultado = multiplicar(primeiro_numero, segundo_numero)
        print(f"\nResultado de {primeiro_numero:.2f} x {segundo_numero:.2f} = {resultado:.2f}")
    else:
        resultado = dividir(primeiro_numero, segundo_numero)
        print(f"\nResultado de {primeiro_numero:.2f} / {segundo_numero:.2f} = {resultado:.2f}")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

if(__name__ == "__main__"):
    display()