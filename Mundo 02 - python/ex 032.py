from random import randint

print("x" * 35)
print('\033[1;33mVAMOS JOGAR PAR OU ÍMPAR ?!\033[m')
print("x" * 35)

vitoria = 0

while True:
    a = randint(0, 10)
    valor = int(input('Digite um valor:'))
    tipo = " "
    total = a + valor

    while tipo not in 'PpIi':
        tipo = str(input('PAR ou ÍMPAR:[P/I]')).upper()

    print("x" * 50)
    print(f'\033[1;97mO Jogador jogou {valor} o computador jogou {a} e a soma dos dois valores é {total}.\033[m')
    print("x" * 50)

    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;97mO Jogador Venceu\033[m')
            vitoria += 1
        else:
            print('\033[1;97mVoce perdeu!!\033[m')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;97mO jogador Venceu\033[m')
            vitoria += 1

        else:
            print('\033[1;97mVoce perdeu\033[m')
            break

print("=-=" * 50)
print(f'Voce venceu ao total {vitoria} vezes.')


