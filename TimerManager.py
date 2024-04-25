from SubTask import SubTask
import SubTaskManager
from Timer import Timer
import FileManager
from InputThread import *
from SoundManager import SoundManager
from CalendarTrack import *
import datetime
from Meeting import Meeting

class TimerManager:

    # Initialise an empty array to contain saved configurations
    def __init__(self):
        self.__configurations = []
        self.soundManager = SoundManager()
        self.__meetings = []
        self.__calTrack = CalendarTrack()

    def isValidDateString(self, dateStr):
        # giving the date format
        date_format = '%Y-%m-%d'
        try:
            # formatting the date using strptime() function
            _dateObject = datetime.datetime.strptime(dateStr, date_format)
            return True

        # If the date validation goes wrong
        except ValueError:
            return False

    # Manage the timer logic
    def run(self):
        isRunning = True
        
        self.__configurations = FileManager.loadConfigs("ConfigInfo.csv")
        self.__calTrack.loadCalendar()
        self.__calTrack.sendNotification()
        
        # Program keeps looping the main menu until the loop is exited by entering the exit code.
        while isRunning:
            
            # Print the main menu and get user selection
            userSelection = self.mainMenu()

            # If 1 is selected create a new Configuration object with input name and append it to the saved configs list
            if userSelection == "1":
                self.createNewConfiguration()

            #Export a configuration
            elif userSelection == "2":
                self.exportConfiguration()

            # Import a configuration
            elif userSelection == "3":
                self.importConfiguration()

            # Run timer from config
            elif userSelection == "4":
                self.runTimer()
            
            # Allow the user to modify the configuration
            # First prompt the user for which configuration they want to modify
            # After we know which configuration, we then allow user to modify, add, remove the subtask inside that configuration
            elif userSelection == "5":
                self.modifyConfiguration()

            # develop one feature to enhance countdown timer, which can be used to support online meetings
            elif userSelection == "6":
                self.showMeetingMenu()

            # Feature 5 - Sound
            elif userSelection == "7":
                self.setSoundSettings()

            # Exit application
            elif userSelection == "8":
                isRunning = False
                FileManager.saveConfigs("ConfigInfo.csv", self.__configurations)
                self.__calTrack.saveCalendar()

            # Incorrect input
            else:
                print("Please enter a valid selection as an integer 1-8")


    def createNewConfiguration(self):
        configNameIn = getInput("Enter new configuration name: ")
        newConfig = SubTaskManager.createConfiguration(configNameIn)

        # Ask user for subtask names & durations repeatedly until user chooses not to.
        isContinue = True

        while isContinue:

            subTaskName = getInput("Enter the new subtask name (leave blank to end): ")
            if subTaskName == "":
                isContinue = False
            else:
                subTaskDuration = ""
                while (not subTaskDuration.isdigit()):
                    subTaskDuration = getInput("Enter the time in minutes for subtask: ")
                
                newSubTask = SubTask(subTaskName, int(subTaskDuration) * 60)
                newConfig.addSubTask(newSubTask)

        self.__configurations.append(newConfig)
        print("Configuration created.")

        # Once a config has been created, the user is prompted to add a reminder for the future.
        calendarInput = getInput("Would you like to add a reminder for the config? Y/N")

        if calendarInput.lower() == "y":
            dateInput = getInput("What date will the reminder send a notification?")
            while not self.isValidDateString(dateInput):
                print("Incorrect data format, should be YYYY-MM-DD")
                dateInput = getInput("What date will the reminder send a notification?")
                
            self.__calTrack.addToCalendar(configNameIn, dateInput)
        
        
    def exportConfiguration(self):
        inputFailure = True
        while inputFailure:
            inputFailure = False

            configIndexIn = getInput("Enter the index of the configuration you would like to export: ")
            try:
                FileManager.outputConfig(self.__configurations[int(configIndexIn)])
                print("Configuration exported.")
            except:
                print("Invalid selection, please enter an integer corresponding to the configuration index (starting from 0).")
                inputFailure = True

    def importConfiguration(self):
        filenameIn = getInput(
            "Enter the name of the configuration you would like to import: ")
        importedConfig = FileManager.inputConfig(filenameIn)
        self.__configurations.append(importedConfig)
        print("Configuration imported successfully.")

    def runTimer(self):
        configIndexIn = int(getInput("Enter the index of the configuration you would like to run (input from 0): "))

        # prompt the user again if they enter incorrectly or enter the word
        while configIndexIn < 0 or configIndexIn >= len(self.__configurations):
            print("Invalid index")
            configIndexIn = int(getInput("Enter the index of the configuration you would like to run: "))
        config = self.__configurations[configIndexIn]

        print("Type 'p' to pause the time")
        print("Type 'r' to resume the time")
        print("Type 'a' to advance the time")
        print("Type 'e' to extend the time")

        # Runs each subtask in the chosen config sequentially.
        subTaskList = config.subTasks
        for subTask in subTaskList:
            print("Start", subTask.name)
            timer = Timer(subTask.length, self.soundManager)
            timer.countDown()

    def modifyConfiguration(self):
        configIndexIn = int(getInput("Enter the index of the configuration you would like to modify (Index must start from 0): "))
        # prompt the user for input again if they enter incorrectly
        while configIndexIn < 0 or configIndexIn >= len(self.__configurations):
            print("Invalid index")
            configIndexIn = int(getInput("Enter the index of the configuration you would like to modify (Index must start from 0): "))

        config = self.__configurations[configIndexIn]
        subTaskList = config.subTasks
        isContinue = True

        while isContinue:
            print("Please make a selection:")
            print("1. Modify a subtask")
            print("2. Add a subtask")
            print("3. Remove a subtask")
            print("4. Exit configuration menu")
            userSelection = getInput("Enter selection: ")

            if userSelection == "1":
                subTaskIndexIn = int(getInput("Enter the index of the subtask you would like to modify (Index must start from 0): "))
                # prompt the user for input again if they enter incorrectly
                while subTaskIndexIn < 0 or subTaskIndexIn >= len(subTaskList):
                    print("Invalid index")
                    subTaskIndexIn = int(getInput("Enter the index of the subtask you would like to modify (Index must start from 0): "))
                
                subTask = subTaskList[subTaskIndexIn]
                isContinue = True

                while isContinue:
                    print("Please make a selection:")
                    print("1. Modify subtask name")
                    print("2. Modify subtask duration")
                    print("3. Exit subtask menu")
                    userSelection = getInput("Enter selection: ")
                    
                    # verify the user input and prompt them for input again if entered incorrectly
                    while userSelection != "1" and userSelection != "2" and userSelection != "3":
                        print("Please enter a valid selection as an integer 1-3")
                        userSelection = getInput("Enter selection: ")

                    if userSelection == "1":
                        subTaskNameIn = getInput("Enter new subtask name: ")
                        subTask.name = subTaskNameIn
                        
                    elif userSelection == "2":
                        subTaskDurationIn = int(getInput("Enter new subtask duration in minutes: "))
                        # run function verifySubTaskDuration() to verify user input for subtask duration
                        self.verifySubTaskDuration(subTaskDurationIn)
                        subTask.length = subTaskDurationIn * 60
                        
                    elif userSelection == "3":
                        # allow user to exit the configuration menu and go back to the Main Menu
                        isContinue = False
                        
                    else:
                        print("Please enter a valid selection as an integer 1-3")

            elif userSelection == "2":
                subTaskNameIn = getInput("Enter the new subtask name: ")
                subTaskDurationIn = int(getInput("Enter the new subtask duration in minutes: "))
                # run function verifySubTaskDuration() to verify user input for subtask duration
                self.verifySubTaskDuration(subTaskDurationIn)
                
                newSubTask = SubTask(subTaskNameIn, subTaskDurationIn * 60)
                subTaskList.append(newSubTask)

            elif userSelection == "3":
                subTaskIndexIn = int(getInput("Enter the index of the subtask you would like to remove (Index must start from 0): "))
                subTaskList.pop(subTaskIndexIn)

            elif userSelection == "4":
                isContinue = False

            else:
                print("Please enter a valid selection as an integer 1-4")

    def showMeetingMenu(self):
        isContinue = True
                
        while isContinue:
            print("Please make a selection:")
            print("1. Create a new meeting")
            print("2. Join a meeting")
            print("3. Exit meeting menu")
            userSelection = getInput("Enter selection: ")
            
            # verify the user input and prompt them for input again if entered incorrectly
            while userSelection != "1" and userSelection != "2" and userSelection != "3":
                print("Please enter a valid selection as an integer 1-3")
                userSelection = getInput("Enter selection: ")
                
            if userSelection == "1":
                meetingName = getInput("Enter the name of the meeting: ")
                meetingPassword = getInput("Enter the password of the meeting: ")
                meetingDuration = int(getInput("Enter the duration of the meeting in minutes: "))
                # run function verifySubTaskDuration() to verify user input for meeting duration
                self.verifySubTaskDuration(meetingDuration)
                
                newMeeting = Meeting(meetingName, meetingPassword, meetingDuration * 60)
                self.__meetings.append(newMeeting)
                print("Meeting created successfully.")
                
            elif userSelection == "2":
                # allow user to join the meeting they created successfully by inputting the correct name and password of the meeting they set before
                meetingName = getInput("Enter the name of the meeting: ")
                meetingPassword = getInput("Enter the password of the meeting: ")
                
                # display error and prompt user for input again if the meeting information is not found in the storage
                while not any(meeting.name == meetingName and meeting.password == meetingPassword for meeting in self.__meetings):
                    print("Invalid meeting name or password")
                    meetingName = getInput("Enter the name of the meeting: ")
                    meetingPassword = getInput("Enter the password of the meeting: ")
                
                # display the meeting information and allow user to join the meeting
                for meeting in self.__meetings:
                    if meeting.name == meetingName and meeting.password == meetingPassword:
                        print("Meeting name: ", meeting.name)
                        print("Meeting password: ", meeting.password)
                        print("Meeting duration: ", meeting.duration/60, "minutes")
                        print("Your meeting starts now!")
                        
                        timer = Timer(meeting.duration, self.soundManager)
                        timer.countDown()
                
            elif userSelection == "3":
                isContinue = False
                
            else:
                print("Please enter a valid selection as an integer 1-3")
    

    def setSoundSettings(self):
        print("Sound Settings")
        print("Please make a selection:")
        print("1. Toggle sounds on/off (currently ",end="")

        # Show current sound toggle status
        if(self.soundManager.enabled):
            print("on)")
        else:
            print("off)")

        # Manage user selection
        soundMenuSelection = getInput("")
        soundMenuInputFailure = True
        while soundMenuInputFailure:
            soundMenuInputFailure = False

            if soundMenuSelection == "1":
                self.soundManager.enabled = not self.soundManager.enabled
            else:
                soundMenuInputFailure = True
                print("Please enter a valid selection as an integer")
    

    # Print the main menu information and take in user selection
    def mainMenu(self):
        print("Main Menu")
        print("Please make a selection:")
        print("1. Create new configuration")
        print("2. Export a configuration")
        print("3. Import a configuration")
        print("4. Run timer from a configuration")
        print("5. Modify a configuration")
        print("6. Meeting menu")
        print("7. Set sound settings")
        print("8. Exit application")

        if len(self.__configurations) != 0:
            print("Current configurations:")
            self.showConfigurations()
        
        # Kill the input thread
        userSelection = getInput("Enter selection: ", "8")

        return userSelection

    # Print all currently saved configurations
    def showConfigurations(self):

        for i, configuration in enumerate(self.__configurations):
            print(str(i) + ":", configuration)

    # Print all saved subtasks
    def showSubTasks(self):
        for configuration in self.__configurations:
            for subTask in configuration.subTasks:
                print(subTask)
    
    # function to verify if user enters the subtask duration correctly and if not, prompt them again
    def verifySubTaskDuration(self, subTaskDurationIn):
        while subTaskDurationIn < 0:
            print("Please enter a valid duration for the subtask")
            subTaskDurationIn = int(getInput("Enter the new subtask duration in minutes: "))
        return subTaskDurationIn

startInputThread()
test = TimerManager()
test.run()
