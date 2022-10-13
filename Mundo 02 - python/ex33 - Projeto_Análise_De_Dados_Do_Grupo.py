maiores = homem = mulheres = 0

while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('IDADE:'))
    sexo = str(input('SEXO:'))
    print('-' * 30)
    continuar = " "

    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in "Ff":
        if idade <= 20:
            mulheres += 1

    while continuar not in 'SsNn':
        continuar = str(input("Deseja continuar?[S/N]"))

    if continuar in 'Nn':
        break

print(f'O total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulheres} mulehres com menos de 20 anos.')
