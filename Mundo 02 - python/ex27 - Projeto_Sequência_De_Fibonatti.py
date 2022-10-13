print("SEQUENCIA DE FIBONATTI")
print("*-*" * 30)
anterior = 0
proximo = 1
soma = 1

termos = int(input("Digite quantos termos você deseja ver:"))
for c in range(1, termos):
    print("\033[1;97m{} - \033[m".format(anterior), end="")
    soma = proximo + anterior
    anterior = proximo
    proximo = soma

print("FIM")
