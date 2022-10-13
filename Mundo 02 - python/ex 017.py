frase = str(input("Digite a frase:")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print("o inverso de {} é {}.".format(junto, inverso))
    print("A frase digitada é um PALÍNDROMO.")

else:
    print("o Inverso de {} é {}".format(junto, inverso))
    print('A frase digitada NÃO é um PALÍNDROMO.')

