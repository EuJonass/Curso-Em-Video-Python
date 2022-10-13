n0 = float(input("Primeira nota:"))
n1 = float(input("Segunda nota:"))

print("=-=" * 50)
resultado = (n0 + n1) / 2

if resultado >= 7:
    print("ALuno aprovado")
    print("Com a média das notas {:.1f} e {:.1f} obtemos {:.1f}, que esta acima da média desejada.".format(n0, n1, resultado))

elif resultado < 7:
    print("Aluno Reprovado")
    print("Com a média das notas {:.1f} e {:.1f} obtemos {:.1f}, que esta abaixo da média desejada.".format(n0, n1, resultado))

elif 7 > resultado >= 5:
    print("O aluno esta de recuperação.")
