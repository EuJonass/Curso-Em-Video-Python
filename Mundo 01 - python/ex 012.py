print("=" * 50)
p = float(input("Qual o preço do produto, sem o desconto ?R$"))
print("=" * 50)
d = float(input("Qual a porcentagem de desconto ?%"))
k = p * d / 100
e = p - k
print("=" * 50)
print("O produto que custava R${:.2f}. Custa agora R${:.2f} com {:.0f}% de desconto.".format(p, e, d))
