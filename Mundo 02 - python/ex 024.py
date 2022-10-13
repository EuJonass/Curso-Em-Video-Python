from time import sleep
valor1 = float(input("Digite o primeiro valor:"))
valor2 = float(input("Digite o segundo valor:"))
opcao = 0
print("O que você deseja fazer com os numeros:")

while opcao != 5:
    sleep(1)
    print("\033[m+*+" * 30)
    print('''    [ 1 ] Somar
    [ 2 ] Multipliar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input("\033[1;97mDigite a opção desejada:\033[m"))

    if opcao == 1:
        soma = valor1 + valor2
        print("\033[1;93mVoce escolheu SOMA!")
        print("\033[1;93mO resultado da soma dos valores {} e {} é {}".format(valor1, valor2, soma))

    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print("\033[1;93mVocê escolheu MULTIPLICAR!")
        print("\033[1;93mO resultado da multiplicação entre os números {} e {} é {}".format(valor1, valor2, multiplicacao))

    elif opcao == 3:
        print("\033[1;93mVoce escolheu MAIOR!")
        if valor1 > valor2:
            print("\033[1;93mO maior numéro foi o {}.".format(valor1))

        elif valor1 < valor2:
            print("\033[1;93mO maior valor foi {}.".format(valor2))

        elif valor1 == valor2:
            print("\033[1;93mOs dois valores são iguais.")

    elif opcao == 4:
        print("Você escolheu a opção NOVOS NÚMEROS.")
        valor1 = float(input("Digite o primeiro valor:"))
        valor2 = float(input("Digite o segundo valor:"))

print("Você escolehu saír! Volte sempre :)")
