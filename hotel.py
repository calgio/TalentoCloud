#Contador de andar do hotel

andares = 20
andar = 0
decrescente = []

while andar <= andares:
    if andar != 13:
        decrescente.append(andar)
    andar = andar + 1

decrescente.sort(key=int, reverse=True)
print(decrescente)
    
