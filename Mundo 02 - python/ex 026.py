print("GERADOR DE PA")
print("+*+" * 10)

primeirotermo = int(input("Primeiro termo da PA:"))
razao = int(input("Razão da PA:"))
termo = primeirotermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1;97m{} ↦\033[m'.format(termo), end="")
        termo += razao
        cont +=1
    print("PAUSA")
    mais = int(input("Quantos t6ermos você quer mostrar a mais?"))
print("Progressão finalizada com {} termos mostrados.".format(total))