import pygame
import pygame.midi

pygame.midi.init()

##############################################################################

class KeyReader(object):
    def __init__(self):
        self._input = pygame.midi.Input(0)
        self._active = False
    def read(self):
        self._active = True
        while self._active:
            if self._input.poll():
                yield self._input.read(1)[0]
        
reader = KeyReader()
for k in reader.read():
    print k
