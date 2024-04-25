# Run from command line in parent directory using "python -m testing.SoundManager_Testing"
from SoundManager import SoundManager
import time

def testBeepEnabled():
    testManager = SoundManager()
    testManager.playBeep()

def testBeepDisabled():
    testManager = SoundManager()
    testManager.enabled = False
    testManager.playBeep()

print("Testing beep disabled.")
testBeepDisabled()
time.sleep(3)

print("Testing beep enabled.")
testBeepEnabled()