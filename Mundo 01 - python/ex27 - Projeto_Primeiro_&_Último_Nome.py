f = str(input("Digite seu nome:")).strip()
n = f.split()
print("É um prazer te conhecer!")
print("Seu primeiro nome é {}".format(n[0]))
print("Seu último nome é {}".format(n[len(n)-1]))
