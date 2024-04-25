from datetime import timedelta

# Contain the label (name) and time in seconds (length) of an individual timer configuration subtask


class SubTask:

    # Initialise private instance variables 'name' and 'length'
    def __init__(self, nameIn, lengthIn):
        self.__name = nameIn
        self.__length = lengthIn

    # Return string representation of the SubTask object with length converted from seconds to TimeDelta string (hours:minutes:seconds)
    def __str__(self):
        return "{:<20} {:>10}".format(self.__name, str(timedelta(seconds=self.__length)))

    # Getters and setters for the two instance variables, defined as properties to implement private variable safety
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nameIn):
        self.__name = nameIn

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, lengthIn):
        self.__length = lengthIn
