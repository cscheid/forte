import pygame
import pygame.midi

has_init = False
def init_midi_interface():
    global has_init
    if not has_init:
        pygame.midi.init()
        has_init = True

##############################################################################

class KeyReader(object):
    def __init__(self):
        init_midi_interface()
        self._input = None
        for i in xrange(pygame.midi.get_count()):
            interf, name, is_input, is_output, is_open = pygame.midi.get_device_info(i)
            if is_input:
                print interf, name
                self._input = pygame.midi.Input(i)
                break
        if self._input is None:
            raise Exception("found no usable midi inputs")
        self._active = False
    def read(self):
        self._active = True
        while self._active:
            if self._input.poll():
                yield self._input.read(1)[0]
