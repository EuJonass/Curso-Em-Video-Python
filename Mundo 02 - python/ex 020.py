sexo = 0
maiorvelho = 0
nomevelho = " "
soma = 0
totmulher = 0

for p in range(1, 5):
    print("----- {}ª PESSOA -----".format(p))
    nome1 = str(input("NOME:")).upper().strip()
    idade1 = int(input("IDADE:"))
    sexo1 = str(input("SEXO [M/F]:")).upper().strip()
    soma += idade1 / 4

    if p == 1 and sexo1 == "M":
        maiorvelho = idade1
        nomevelho = nome1
    if sexo1 == "M" and idade1 > maiorvelho:
        maiorvelho = idade1
        nomevelho = nome1
    elif sexo1 =="F" and idade1 < 20:
        totmulher += 1

print("\033[32m------ RESOLUÇÃO ------\033[m")
print("A média da idade do grupo é de {} anos.".format(soma))
print("O homem mais velho do grupo tem {} anos e se chama {}.".format(maiorvelho, nomevelho))
print("Ao todo tem {} mulheres com menos de 20 anos.".format(totmulher))

