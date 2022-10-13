print('=' * 28)
print('         BANCO CEV')
print('=' * 28)

valor_saque = int(input('Digite o valor para saque:'))
total = valor_saque
ced = 50
totaldeced = 0

while True:
    if total >= ced:
        total -= ced
        totaldeced += 1

    else:
        if totaldeced> 0:
            print(f'Total de {totaldeced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaldeced = 0
        if total == 0:
            break

print('\033[1;31m=' * 46)
print('        BANCO CEV DESEJA UM BOM DIA\033[M')
print('=' * 46)