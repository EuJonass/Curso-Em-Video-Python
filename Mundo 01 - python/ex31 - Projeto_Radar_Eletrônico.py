print("-=-" * 50)

c = int(input("Qual a velocidade atual do carro?"))
multa = (c - 80) * 7
print("-=-" * 50)

if c <= 80:
    print("Siga com cuidado! Tenha um bom dia!")
else:
    print("MULTADO!! Você excedeu o limite da 80Km/h da via\nVocê deve pagar uma multa de R${:.2f}!".format(multa))

print("-=-" * 50)
