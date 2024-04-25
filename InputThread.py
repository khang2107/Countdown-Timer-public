import threading
import time

class InputThread:
    
    # Initialise variables used for InputThread class.
    def __init__(self):
        self.__running = True
        self.enteredText = None
        self.killCommand = None

    # Start the thread
    def startThread(self):
        inputThread = threading.Thread(target=self.__userInputTaker)
        inputThread.start()

    # A blocking function that listens for inputs continuously. Each
    # user input string is assigned to enteredText. The function returns
    # when a killCommand is inputted by the user.
    def __userInputTaker(self):

        while self.__running:
            userInput = input()
            self.enteredText = userInput
            if (userInput == self.killCommand):
                return

_instance = InputThread()

def startInputThread():
    _instance.startThread()

# A blocking function that waits for the response from the inputThread
# then returns the response.
def getInput(text="", killCommand=None):
    _instance.killCommand = killCommand
    if text != "":
        print(text)

    while True:
        result = input_poll()
        if result != None:
            return result
        else:
            time.sleep(0.1)

# A non-blocking function that queries the inputThread for new user input.
# if there is new user input, the function returns that input, otherwise
# returns None.
def input_poll():
    if _instance.enteredText != None:
        result = _instance.enteredText
        _instance.enteredText = None
        return result
    else:
        return None
