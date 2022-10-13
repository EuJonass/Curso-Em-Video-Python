from time import sleep
import pygame

v = str(input("Digite SIM ou NÂO para escolher se havera som de fogos ou não.")).lower()

if v == "sim" or v == "s":
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    pygame.init()
    pygame.mixer.music.load("ex 009 fogos.mp3")
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

elif v == "não" or v == "nao" or v == "n":
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    pygame.init()
    pygame.mixer.music.load("gemido ex 009.mp3")
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    print("Acabou")
