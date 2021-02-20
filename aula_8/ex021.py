# Faça um programa que abra e reproduaza o audio de um arquivo em MP3

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')