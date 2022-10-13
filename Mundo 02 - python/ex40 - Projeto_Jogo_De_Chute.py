from random import randint

random = randint(0, 15)
chute = 0
chances = 10

print("=-=" * 40)
print('#### Iníciando Jogo ####')
print("=-=" * 40)


while chute != random:
    chute = input('Chute um número entre 0 a 15: ')

    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print(' ')
            print('-=-' * 50)
            print(f'Parabéns, você venceu! O número era {random} e você ainda tinha {chances} chances.')
            break

        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É um número menor.')
                print("=-=" * 50)
            else:
                print('Você errou!!! Dica: É um número maior.')
            print(f'Você ainda possui {chances} chances.')
            print(' ')

        if chances == 0:
            print(' ')
            print('Suas chances acabaram, você perdeu!')
            print(' ')
            break

print("#### Fim do Jogo ####")
