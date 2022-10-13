soma = 0 #acumulador
cont = 0 #contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1

print("-x-" * 40)
print("A soma de todos os {} valores solicitados é {}.".format(cont, soma))
print("-x-" * 40)
