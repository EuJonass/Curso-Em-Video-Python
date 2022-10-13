from random import shuffle
print("=" * 50)

n1 = str(input("Digite o nome:"))
print("=" * 50)
n2 = str(input("Digite o nome:"))
print("=" * 50)
n3 = str(input("Digite o nome:"))
print("=" * 50)
n4 = str(input("Digite o nome:"))
print("=" * 50)
l = [n1, n2, n3, n4]
a = shuffle(l)

print("=" * 30)
print("O escolhido foi {}".format(l))
print("=" * 50)
