soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {} número:".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Voce informou {} números PARES e a soma deles é {}.".format(cont, num))
