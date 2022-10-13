from random import randint

print("-=-" * 50)

print("Vou pensar em um número de 0 a 5. Tente advinhar...")

print("-=-" * 50)
s = randint(0, 5)
n = int(input("Em qual número pensei ?"))
print("PROCESSANDO....")

print("-=-" * 50)

if n == s:
    print("Você acertou, o número escolhido por mim foi {}, PARABENS!".format(s))
else:
    print("Você erro! :(")


