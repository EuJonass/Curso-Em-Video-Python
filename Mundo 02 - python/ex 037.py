temperatura = int(input('Qual a temperatura?'))

if temperatura <= 48:
    print('A carne esta selada')

elif 48 < temperatura > 54:
    print(' A carne esta ao ponto para mal')

elif 54 < temperatura > 60:
    print('A carne está ao ponto')

elif 60 < temperatura > 65:
    print('A carne esta ao ponto para bem')

elif 65 < temperatura > 71:
    print('A carne esta mal passada')