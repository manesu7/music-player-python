import os
import pygame

pygame.mixer.init()

songs = [f for f in os.listdir("music") if f.
         endswith(".mp3")]

for song in songs:
    print(f"Now playing: {song}")
    pygame.mixer.music.load(f"music/{song}")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      pass