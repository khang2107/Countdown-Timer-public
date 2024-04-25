import time
from InputThread import *
from SoundManager import SoundManager

class Timer:

    # Initialise variables used for Timer class.
    def __init__(self, duration, soundManager):
        self.__duration = duration
        self.__isTicking = True
        self.__isRunning = True
        self.__soundManager = soundManager

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, time):
        self.__duration = time

    def fetchInput(self):
        return input_poll()
    
    # The function queries the key pressed by the user and handles
    # the input by changing state accordingly.
    def keyHandler(self):
        userInputStr = self.fetchInput()
        if userInputStr == None:
            return
        
        for userInput in userInputStr:
            if userInput == "p": # pause
                self.__isTicking = False
            if userInput == "r": # resume
                self.__isTicking = True
            if userInput == "a": # advance
                self.__isRunning = False
            if userInput == "e": # extend
                self.__isRunning = True
                print("")
                print("How long would you like to extend?")
                extendInput = getInput()
                self.__duration += int(extendInput) * 60     

    def waitOneSecond(self):
        time.sleep(1)

    def showTimer(self, time):
        print("", end="\r")
        print(time, end="")

    # This is a blocking function that makes the timer tick until it runs out of time.
    def countDown(self):
        while self.__duration >= 0 and self.__isRunning:
            self.tick()
        print("")
        print("Time is up!")
        if self.__soundManager.enabled:
            self.__soundManager.playBeep()

    # Ticks the time by one second, displays the time to the user and processes user input.
    def tick(self):
        mins, secs = divmod(self.__duration, 60)
        timer = '  {:02d}:{:02d}         '.format(mins, secs)
        self.showTimer(timer)
        self.waitOneSecond()
        self.keyHandler()
        if self.__isTicking:
            self.__duration -= 1