print("=-=" * 30)
n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))
n4 = float(input("Digite um número:"))
menor = n1
maior = n1

#Verificação quem é menor!
if n2 < n1 and n2 < n3 and n2 < n4:
    menor = n2
if n3 < n1 and n3 < n2 and n3 < n4:
    menor = n3
if n4 < n1 and n4 < n2 and n4 < n3:
    menor = n4

#verificação quem é maior!
if n2 > n1 and n2 > n3 and n2 > n4:
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3:
    maior = n4

print("=-=" * 30)
print("O maior número é {}!".format(maior))
print("=-=" * 30)
print("O menor número é {}!".format(menor))
print("=-=" * 30)