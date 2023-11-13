#Função Calculadora


def soma(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2

aux = True

while aux:

    op = int(input("Digite o operador para operação: 1 = Soma; 2 = Subtação; 3 = Multiplicação; 4 = Divisão; 0 - Sair."))

    if op == 1:
        num1 = float(input("Digite o primeiro número para calcular:"))
        num2 = float(input("Digite o segundoi número para calcular:"))
        print(soma(num1, num2))

    if op == 2:
        num1 = float(input("Digite o primeiro número para calcular:"))
        num2 = float(input("Digite o segundoi número para calcular:"))
        print(sub(num1, num2))

    if op == 3:
        num1 = float(input("Digite o primeiro número para calcular:"))
        num2 = float(input("Digite o segundoi número para calcular:"))
        print(mult(num1, num2))

    if op == 4:
        num1 = float(input("Digite o primeiro número para calcular:"))
        num2 = float(input("Digite o segundoi número para calcular:"))
        print(div(num1, num2))

    if op == 0:
        break



