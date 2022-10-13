n = int(input("Digite um número inteiro:"))

print("Escolha uma das bases de conversão abaixo:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para HEXADECIMAL")
print("[ 3 ] converter para OCTA")

print("=-=" * 50)

#CONVERTEMOS O  VALOR DIGITADO PARA BINARIO, HEXADECIMAL E OCTA
bin = bin(n)[2:]
hex = hex(n)[2:]
oct = oct(n)[2:]

a = int(input("DIGITE A SUA OPÇÃO DE ESCOLHA:"))

if a == 1:
    print("VOCE ESCOLHEU BINARIO")
    print("O valor {} digitado em BINÁRIO é {}".format(n, bin))

elif a == 2:
    print("VOCE ESCOLHEU HEXADECIMAL")
    print("O valor {} digitado em HEXADECIMAL é {}".format(n, hex))

elif a == 3:
    print("VOCE ESCOLHEU OCTA")
    print("O valor {} digitado em OCTA é {}".format(n, oct))

else:
    print("SUA ESCOLHA NÃO CORRESPONDE A NENHUMA ALTERNATIVA PROPOSTA! \nTENTE MOVAMENTE!")

