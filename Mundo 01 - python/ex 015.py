print("X" * 60)

c = float(input("Qauntos dias você ficou com o carro?"))
print("X" * 60)
k = float(input("Quantos KM você rodou com o carro?"))
print("X" * 60)
c1 = float(input("Qual a diária do carro?R$"))
print("X" * 60)
k1 = float(input("Qual foi o preço por KM rodado?R$"))
km = k * k1
ca = c * c1
k2 = km + ca

print("X" * 60)
print("O Valor total a pagar é de R${:.2f}".format(k2))
