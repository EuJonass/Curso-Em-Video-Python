from random import randint
cont = 0
n = 0
print("+=+" * 20)
print("Vou pensar em um número de 0 a 10. Tente advinhar...")
s = randint(0, 10)

while n != s:
    n = int(input("Em qual número pensei ?"))
    cont += 1
    if n < s:
        print("\033[32mchute um valor mais alto.\033[m")
    elif n > s:
        print("\033[32mchute um valor mais baixo.\033[m")
    print("+=+" * 25)
print("\033[1;34mAcabou !! Você precisou de {} chutes".format(cont))