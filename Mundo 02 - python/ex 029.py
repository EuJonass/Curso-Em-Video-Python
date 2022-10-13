soma = cont = 0
while True:
    pergunta = int(input("Digite um número:"))
    if pergunta != 999:
        cont += 1

    elif pergunta == 999:
        break
    soma += pergunta

print(f"Foram digitados {cont} números e a soma entre eles é de {soma}.")