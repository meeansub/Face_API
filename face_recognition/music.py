import pygame
import time

class PlayMusic(object):
    def __init__(self) :
        self.mixer.music.load()

        time.sleep(10)
    def __del__(self):
        self.mixer.music.stop()

    def play(self):
        self.mixer.music.play()

if __name__ == '__main__' :
    pygame = PlayMusic()

    pygame.mixer.music.load(a.wav)
