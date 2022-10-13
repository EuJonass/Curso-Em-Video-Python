s = int(input("Apartir de qual numero par voce deseja começar:"))
n = int(input("Ate que número:"))

for c in range(s, n + 2,  2):
    print(c, end=' ')
