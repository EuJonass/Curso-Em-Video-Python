from datetime import date

ano = int(input("Ano do seu nascimento:"))
atual = date.today().year
idade = atual - ano

print("=-=" * 50)
print("O atleta tem {} anos.".format(idade))
print("=-=" * 50)

if idade <= 9:
    print("Classificação: MIRIM")

elif 9 < idade <= 14:
    print("Classificação: INFANTIL")

elif 14 < idade <= 19:
    print("Classificação: JUNIOR")

elif 19 < idade <= 25:
    print("Classificação: SÊNIOR")

elif idade > 25:
    print("Classificação: MASTER")

print("=-=" * 50)
