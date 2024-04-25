import calendar
from datetime import date
import csv
import os.path

class CalendarTrack:

    def __init__(self):
        self.__calendar = dict()

    # Informs the user of any configurations that are scheduled for today.
    def sendNotification(self):
        
        for k, v in self.__calendar.items():
            
            if k == str(date.today()):
                print()
                stringOutput = ", ".join(v)
                print("TIME TO DO", stringOutput.upper(), "!!!")
                print()
                
    def getCalendar(self):
        return self.__calendar
    
    # Adds a config to the calendar. 
    # configName is a string that references the config.
    # calendarIn is a string containing the date to schedule for.
    def addToCalendar(self, configName, calendarIn):
        configNameList = self.__calendar.get(calendarIn)
        if configNameList is None:
            configNameList = []
        configNameList.append(configName)

        self.__calendar[calendarIn] = configNameList 

    # Writes the current calendar to a CSV file.
    def saveCalendar(self):

        with open("CalendarInfo.csv", "w", newline='') as csvFile:

            writeFile = csv.writer(csvFile)

            for date, nameList in self.__calendar.items():
                for name in nameList:
                    writeFile.writerow([date, name])
            csvFile.close()

    # Loads the calendar information from a CSV file.
    def loadCalendar(self):
        if os.path.exists("CalendarInfo.csv"):
            with open("CalendarInfo.csv", "r", newline='') as csvFile:
                readFile = csv.reader(csvFile)
                
                for cal in readFile:
                    configDate = cal[0]
                    configTitle = cal[1]
                    self.addToCalendar(configTitle, configDate)
                csvFile.close()
        return self.__calendar