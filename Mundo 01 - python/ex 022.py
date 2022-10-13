print("=" * 35)

f = str(input("Digite o seu nome:")).strip()
n = f.split()
print("=" * 35)

print("Seu nome maiúsculo fica {}.".format(f.upper()))
print("Seu nome em minúsculo fica {}.".format(f.lower()))
print("Seu nome possue {} letras.".format(len(f)-f.count(" ")))
print("Seu primeiro nome é {} e possue {} letras.".format(n[0], len(n[0])))

print("=" * 35)
