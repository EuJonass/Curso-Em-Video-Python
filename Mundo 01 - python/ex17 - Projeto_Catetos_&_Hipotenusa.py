from math import hypot
'''
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hi= (ca ** 2 + co ** 2) ** (1/2)

print("\n**************************\n")
print("O valor da hipotenusa é: {:.2f}".format(hi))
'''

c1 = float(input("Entre com o valor do cateto oposto: "))
c2 = float(input("Entre com o valor do cateto adjacente: "))
h = hypot(c1, c2)
print("A Hipotenusa ira medir {:.2f}".format(h))
