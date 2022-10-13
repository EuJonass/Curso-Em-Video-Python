from datetime import date

a = int(input("Qual o ano do seu nascimento:"))
atual = date.today().year
idade = atual - a

print("Quem nasceu em {} tem {} anos em {}".format(a, idade, atual))

if idade == 18:
    print("voce deve se alistar esse ano")

elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("Voce nao precisa se alistar, seu alistamento foi em {} a {} anos atrás.".format(ano, saldo))


elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print("Voce ainda nao pode se alisatar, seu alistamento sera  no ano de {} daqui {} anos.".format(ano, saldo))




