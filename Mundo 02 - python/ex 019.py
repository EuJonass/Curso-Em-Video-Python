maior = 0
menor = 0

for peso in range(1, 6):
    valor = float(input("Digite o peso da {}ª pessoa:".format(peso)))

    if peso == 1:
        maior = valor
        menor = valor

    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

print("=x=" * 55)
print("O maior peso lido foi {}kg.\nO menor peso lido foi {}kg.".format(maior, menor))

