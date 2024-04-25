import SubTask

# Create and contain SubTask objects in a list


class Configuration:

    # Initialise instance variable with an empty list
    def __init__(self, nameIn):
        self.__subTasks = []
        self.__name = nameIn

    # Return string representation of Configuration listing name and all SubTasks
    def __str__(self):
        outputString = self.__name.upper() + "\n"

        # Loop through all contained subtasks and append them to output string
        for subTask in self.__subTasks:
            outputString += "    " + str(subTask) + "\n"
        return outputString

    # Getters and setters for the two instance variables, defined as properties to implement private variable safety
    @property
    def subTasks(self):
        return self.__subTasks

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nameIn):
        self.__name = nameIn

    # Add a SubTask to the configuration
    def addSubTask(self, subTaskIn):
        self.__subTasks.append(subTaskIn)

    # Remove a specified SubTask from the configuration
    # Returns True if item was removed, else returns False
    def removeSubTask(self, subTaskIn):
        try:
            self.__subTasks.remove(subTaskIn)
            return True
        except ValueError:
            return False
