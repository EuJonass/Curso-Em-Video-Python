from random import choice

print("=" * 40)
n0 = str(input("Digite o nome do primeiro aluno:"))
print("=" * 40)
n1 = str(input("Digite o nome do segundo aluno:"))
print("=" * 40)
n2 = str(input("Digite o nome do terceiro aluno:"))
print("=" * 40)
n3 = str(input("Digite o nome do quarto aluno:"))
print("=" * 40)
n4 = str(input("Digite o nome do quinto aluno:"))
print("=" * 40)

n = [n0, n1, n2, n3, n4]
e = choice(n)

print("O escolhido foi: {}".format(e))
print("=" * 40)
