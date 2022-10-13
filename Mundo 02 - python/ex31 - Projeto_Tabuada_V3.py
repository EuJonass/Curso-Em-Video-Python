
print("---" * 30)
print('Para para basta digitar ( 0 ).')
while True:
    numero = int(input('\033[;1mDigite um numero para ver sua tabuada:\033[m'))


    if numero == 0:
        break

    for c in range(1, 11):
        vezes = numero * c
        print(f'{numero} x {c} = {vezes}')
