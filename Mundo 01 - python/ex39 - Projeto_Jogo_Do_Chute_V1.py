import random

print("=-=-" * 40)
print("VOCÊ VAI JOGAR O JOGO CHUTE O NÚMERO!!")
print("=-=-" * 40)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
escolha = random.choice(l)

while True:
    n = int(input("Digite um número:"))

    if n == escolha:
        print("VOCÊ ACERTOU PARÁBENS :), o número escolhido foi {}!!".format(escolha))
        break

    elif n < escolha:
        print("Chute um número maior :)")
    else:
        print("Chute um número menor :)")


