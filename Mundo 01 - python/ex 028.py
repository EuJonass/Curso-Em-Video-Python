"""print("-=-" * 50)
c = float(input("Quantos anos tem o seu carro?"))
print("-=-" * 50)

if c <=3:
    print("Seu carro está novinho!")
else:
    print("Seu carro ja está velho em ! :(")

print("--FIM--")"""


# CONDIÇÃO SIMPLIFICADA
print("-=-" * 50)

c = float(input("Quantos anos tem o seu carro?"))
print("Seu carro esta novinho!" if c <= 3 else "Seu carro ja esta velho em !")
print("--FIM--")
