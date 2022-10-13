print("-=-" * 40)

vermelho = "\033[31m"
azul = "\033[1;36;40m"

print("ANALISADOR DE SEGMENTOS")

print("-=-" * 40)


r1 = float(input("Digite o primeiro segmento:"))
r2 = float(input("Digite o segundo segmento:"))
r3 = float(input("Digite o terceiro segmento:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triangulo!")
else:
    print(f"{azul}Os segmentos acima NÃO podem formar um triângulo!")