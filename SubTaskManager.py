from Configuration import Configuration
from SubTask import SubTask


def createConfiguration(name):
    #STUB: TO-DO
    return Configuration(name)

def addSubTask(configurationIn, nameIn, lengthIn):
    #STUB: TO-DO
    return configurationIn.addSubTask(SubTask("testTask", 2))

def removeSubTask(configurationIn, indexIn):
    return configurationIn.removeSubTask(indexIn)

def editSubTask(configurationIn, indexIn, nameIn, lengthIn):
    return configurationIn.editSubTask(indexIn, nameIn, lengthIn)
