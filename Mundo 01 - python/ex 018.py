from math import cos, tan, sin, radians

a = float(input("Digite o Ângulo:"))
c = cos(radians(a))
t = tan(radians(a))
s = sin(radians(a))

print("=" * 40)
print("O ângulo de {:.0f}º tem o SENO de {:.2f}".format(a, s))
print("O ângulo de {:.0f}º tem o COSSENO de {:.2f}".format(a, c))
print("O ângulo de {:.0f}º tem a TANGENTE de {:.2f}".format(a, t))
print("=" * 40)