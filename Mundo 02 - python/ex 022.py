sexo = str(input("DIgite seu sexo? [M/F]")).upper()
while sexo != "M" and sexo != "F":
    if sexo != "M" and sexo != "F":
        sexo = str(input("DADOS INVALIDOS !! DIGITE SEU SEXO NOVAMENTE:?[M/F]")).upper()
        print("=-=" * 30)

m = "MASCULINO - ♂"
f = "FEMININO - ♀"

if sexo == "M":
    print("\033[33mSexo ({}) registrado com sucesso.".format(m))

elif sexo == "F":
    print("\033[33mSexo ({}) registrado com sucesso.".format(f))