numeroCorreto = False

while (numeroCorreto == False):
    try:
        nome = input("Digite seu nome:")
        data_nascimento = int(input("Se você nasceu entre 1922 e 2021, então digite sua data de nascimento:"))
        if data_nascimento > 1922:
            idade = 2022 - data_nascimento
            numeroCorreto = True
            print(nome,"sua idade é:", idade)
    except:
        print("Não foi digitado um número.")
