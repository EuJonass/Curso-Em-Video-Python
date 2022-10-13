print("*" * 50)

f = float(input("Qual o salário atual do funcionário?R$"))
a = float(input("Qual será a porentagem de aumento?%"))
s = f + (f * a / 100)

print("*" * 50)
print("O salário de R${:.2f} vai para R${:.2f} com {:.0f}% de aumento.".format(f, s, a))
print("*" * 50)