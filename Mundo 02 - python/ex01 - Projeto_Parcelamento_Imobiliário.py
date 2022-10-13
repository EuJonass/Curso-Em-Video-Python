casa = float(input("Qual o valor da casa?R$"))
salario = float(input("Qual o seu salário mensal?R$"))
anos = int(input("Em quantos anos você deseja quitar a casa?"))

prestacao = casa / (anos * 12)
porcento = salario * 30 / 100

print("-=-" * 50)

if prestacao >= porcento:
    print("=-=" * 50)
    print("SUA PRESTAÇÃO NÃO FOI APROVADA!!")
    print("=-=" * 50)
    print("A parcela de R${:.2f} é maior do que 30% do seu salário.".format(prestacao))

elif prestacao < porcento:
    print("=-=" * 50)
    print("SUA PRESTAÇÃO FOI APROVADA!!")
    print("=-=" * 50)
    print("Para pagar a casa de R${:.2f} em {:.0f} anos, a parcela mensal será de R${:.0f}.".format(casa, anos, prestacao))





("Para pagar a casa de R${:.2f} em {:.0f} anos, a parcela será de {:.0f}".format(casa, anos, prestacao))
