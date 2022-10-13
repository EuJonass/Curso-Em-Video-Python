print('=' * 45)

n = int(input("Digite o número:"))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
dm = n // 10000 % 10
print("Analisando o número {}".format(n))
print('=' * 45)

print("O número tem {} dezena de milhar.".format(dm))
print("O número tem {} milhar.".format(m))
print("O número tem {} centenas.".format(c))
print("O número tem {} dezenas.".format(d))
print("O número tem {} unidades.".format(u))

print('=' * 45)