print('=' * 30)
print('     LOJA SUPER BARATO')
print('=' * 30)

total = maior = barato = cont = men0r = 0
nomebarato = ' '
while True:
    produto = str(input('Nome do produto:'))
    valor = int(input('Digite o valor do produto:R$'))
    cont += 1
    total += valor
    #barato += valor


    if valor >= 1000:
        maior += 1

    print('=' * 30)

    if barato >= valor:
        nomebarato = produto
        barato = valor

    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input("Deseja continuar?[S/N]")).upper()

    print('=' * 30)

    if continuar in 'Nn':
        break


print('--------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi de R${total}.')
print(f'Tivemos {maior} produtos costando mais de R$1.000')
print(f'O produto mais barato foi {nomebarato} que custou R${menor}')