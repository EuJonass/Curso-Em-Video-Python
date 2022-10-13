'''n = float(input("Digite um número para ver sua tabuada:"))
print("=x=" * 45)
cont = 0
for c in range(1, 11):
    cont = cont + 1
    tb = n * cont
    print("{:.0f} x {:.0f} = {:.0f}".format(n, cont, tb))
print("Programa terminado!")'''


num = int(input("Digite o número para ver sua tabuada:"))
for c in range(1, 11):
    print("{} X {} = {}".format(num, c, num*c))
print("O programa terminou!")