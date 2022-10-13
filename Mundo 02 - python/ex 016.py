numero = int(input("Digite o número:"))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
         print("\033[34m", end=" ")
         cont += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")

print("\033[m\nO número {} foi divisivel {} vezes.".format(numero, cont))

if cont == 2:
    print("E por isso ele é PRIMO.")
else:
    print("E por isso ele NÃO É PRIMO.")