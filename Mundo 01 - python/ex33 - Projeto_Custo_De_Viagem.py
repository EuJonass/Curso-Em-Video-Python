d = int(input("Digite a distância da viagem:"))
if d >= 200:
    f = d * 0.45
    print("Você está prestes a começar uma viagem de {}Km".format(d))
    print("Sua passagem tera um custo de R${:.2f}".format(f))

else:
    f = d * 0.50
    print("Voce está prestes a começar uma viagem de {}Km".format(d))
    print("Sua passagem tera um custo de R${:.2f}".format(f))
