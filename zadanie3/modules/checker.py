from .clock import Clock

class Checker:

    def __init__(self):
        self.clock = Clock()

    def remainder(self):
        if self.clock.getTime().hour > 17:
            self.clock.playWavFile()
            return True
        return False