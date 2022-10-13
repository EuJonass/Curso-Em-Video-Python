from time import sleep
from random import randint
pc = randint(1, 3)
print(pc)
print('''SUAS OPÇÕES
[ 1 ] PEDRA
[ 2 ] PAPEl
[ 3 ] TESOURA''')

pc = randint(1, 3)
jogada = int(input("Qual a sua jogada?"))
sleep(0.25)
print("JO")
sleep(0.15)
print("KEN")
sleep(0.15)
print("PO")
print("==" * 20)

if pc == 1:
    print("O Computador jogou PEDRA")
    if jogada == 1:
        print("O Jogador jogou PEDRA")
        print("--- EMPATE ---")
    elif jogada == 2:
        print("O jogador jogou PAPEL")
        print("--- VITÓRIA DO JOGADOR ---")
    elif jogada == 3:
        print("O Jogador jogou TESOURA")
        print("--- DERROTA ---")

    elif pc == 2:
        print("O Computador jogou PEDRA")
        if jogada == 1:
            print("O Jogador jogou PEDRA")
            print("--- EMPATE ---")
    elif jogada == 2:
        print("O Jogador jogou PAPEL")
        print("--- VITÓRIA ---")
    elif jogada == 3:
        print("O Jogador jogou TESOURA")
        print("--- DERROTA ---")

elif pc == 3:
    print("O Computador jogou TESOURA")
    if jogada == 1:
        print("O Jogador jogou PEDRA")
        print("--- VITÓRIA ---")
    elif jogada == 2:
        print("O Jogador jogou PAPEL")
        print("--- DERROTA ---")
    elif jogada == 3:
        print("O Jogador jogou TESOURA")
        print("--- EMPATE ---")
print("==" * 20)
print()