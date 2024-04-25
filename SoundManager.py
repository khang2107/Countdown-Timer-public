# Manage the output of sounds, beeps are output based on the class variables
class SoundManager:

    # Set beep variables to default to the short beep preset
    def __init__(self):
        self.enabled = True
        
    # Play beepCount number of beeps at the specified frequency and duration, repeating the set for the number of times specified by beepLoop with 'wait' milliseconds wait between sets
    def playBeep(self):
        if self.enabled:
            print('\a')