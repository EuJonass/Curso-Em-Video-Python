f = str(input("Digite seu nome completo:")).strip().lower()
print("A letra 'A' aparece {} nas frases.".format(f.count("a")))
print("A primeira letra 'A' aparece na posição {}.".format(f.find("a")+1))
print("A última letra 'A' aparece na posição {}.".format(f.rfind("a")+1))
