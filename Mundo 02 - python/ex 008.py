print("========= LOJAS JONAS ==========")
preco = float(input("Preço da compra:R$"))

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista no DINHEIRO
[ 2 ] à vista no CARTÂO
[ 3 ] até 2x no CARTÃO
[ 4 ] 3x ou mais no CARTÃO''')
print("===" * 30)
opc = int(input("DIGITE A OPÇÃO DESEJADA:"))

if opc == 1:
    desconto = preco - (preco * 0.10)
    print("O valor final da sua compra será de R${:.2f}.".format(desconto))

elif opc == 2:
    desconto = preco - (preco * 0.50)
    print("O valor final da sua compra será de R${:.2f}.".format(desconto))

elif opc == 3:
    mes = preco / 2
    print("O valor da sua compra será de R${:.2f}, parcelada em 2x de R${:.2f}".format(preco, mes))

elif opc == 4:
    parcela = int(input("Quantas parcelas deseja?"))
    aumento = preco + (preco * 0.20)
    mes = aumento / parcela
    print("Sua compra será parcelada em {:.0f}x de R${:.2f} com juros.\nSua compra vai custar R${:.2f} no final.".format(parcela, mes, aumento))

else:
    opc = 0
    print("x-x" * 50)
    print("----------OPÇÃO INVÁLIDA ERRO 01----------")
    print("x-x" * 50)
