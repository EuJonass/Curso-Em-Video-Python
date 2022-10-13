from datetime import date
a = date.today().year
#cont = 0       #posisvel usar diretamente o ( c ) do for
acumulador = 0
acumuladorb = 0

for c in range(0, 7):
    #cont += 1    #Possivel remover o cont e osar o ( c ) do for.

    n = int(input("Qual o ano de nascimento da {}ª pessoa?".format(c + 1)))     #( c ) do for
    print("=x=" * 40)
    idade = a - n

    if idade >= 18:
        acumulador += 1
    elif idade <= 18:
        acumuladorb += 1

print("\033[34mAo total tivemos {} pessoas maior de idade. \nE {} pessoas de menor de idade.".format(acumulador, acumuladorb))






