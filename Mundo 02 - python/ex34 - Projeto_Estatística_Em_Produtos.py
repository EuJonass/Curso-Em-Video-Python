'''print('=' * 30)
print('     LOJA SUPER BARATO')
print('=' * 30)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Digite o valor do produto:R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input("Deseja continuar?[S/N]")).upper().strip()[0]
    if resp in 'N':
        break
print('--------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi de R${total}.')
print(f'Tivemos {totmil} produtos costando mais de R$1.000')
print(f'O produto mais barato foi {barato} que custou R${menor}')
'''

cont = 0
tot = 0
totm = 0
r1 = 'N'
r2 = 'S'
lista = []
while True:
    nome = str(input('Nome do produto: '))
    p = float(input('Preço: '))
    q = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    tot = tot + p
    lista = lista + [p]
    if p >= 1000:
        totm = totm + 1
    while r1 != 'N':
        continue
    if q == 'N':
        break
print(f'Valor total: {tot :.2f}')
print(f'Produtos + de 1000: {totm}')
print(f'Menor preço: {nome} = {min(lista)}')
