""" Enunciado:
        Faça um programa em Python que abra e reproduza o áudio
        de um arquivo MP3.
"""


import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
pygame.time.wait(10000)
pygame.mixer.music.stop()
