s = float(input("Digite o salário do funcionario:R$"))

"""cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "amarelo":"\033[33m",
         "pb":"\033[7;30m"}"""

if s <= 1250:
    sf = (s * 15 / 100) + s
    print("O salário R${:.2f} passa a ser agora R${:.2f}".format(s, sf))

else:
    sf = (s * 10 / 100) + s
    print("O salário R${:.2f} passa a ser agora R${:.2f}".format(s, sf))
