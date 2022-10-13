n = int(input("Digite um valor: ou digite [999] para parar!"))
cont = 1
soma = n

while n != 999:
    n = int(input("Digite um valor: ou digite [999] para parar!"))
    cont += 1
    soma += n
    s = soma - 999
print("O codigo parou!")
print("Você digitou {} números e soma entre eles é {}.".format(cont -1, s))