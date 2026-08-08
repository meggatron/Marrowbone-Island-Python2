import os
import pygame


def start_audio():
    pygame.mixer.init()


def play_sound(filename):
    path = os.path.join("assets", filename)
    sound = pygame.mixer.Sound(path)
    sound.play()


def play_music(filename):
    path = os.path.join("assets", filename)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()