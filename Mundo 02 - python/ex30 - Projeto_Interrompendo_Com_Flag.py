cont = soma = 0
while True:
    n = int(input("Digite um valor: ou digite [999] para parar!"))
    if n == 999:
        break
    cont += 1
    soma += n

print("O codigo parou!")
print("Você digitou {} números e soma entre eles é {}.".format(cont, soma))
