import Configuration
import SubTask
import csv
import os.path

#Output a csv file based on the input Configuration object
def outputConfig(configurationIn):

    #Open the csv file in write mode
    with open(configurationIn.name + ".csv", "w", newline='') as csvFile:

        #Create csv writer object to write rows to csv file
        writer = csv.writer(csvFile)

        #Loop over all SubTasks in the Configuration object and write them as rows to the file
        for subTask in configurationIn.subTasks:
            writer.writerow([subTask.name, subTask.length])
        csvFile.close()

#Create a Configuration object based on an input CSV file
def inputConfig(fileName):

    #Create the blank Configuration object, name is the input file name
    configOut = Configuration.Configuration(fileName)

    #Open the csv file in read mode
    with open(fileName + ".csv", "r") as csvFile:

        #Create csv reader object to read rows from csv file
        reader = csv.reader(csvFile)

        #Loop over the rows in the csv, assign first column to name variable and second column to length variable
        for subTaskIn in reader:
            name = subTaskIn[0]
            length = int(subTaskIn[1])

            #Create SubTask object using name and length, add the SubTask object to Configuration object
            configOut.addSubTask(SubTask.SubTask(name, length))
        csvFile.close()
    return configOut

def saveConfigs(filename, configurations):
    # Open the csv file in write mode
    with open(filename, "w", newline='') as csvFile:
        # Create csv writer object to write rows to csv file
        writer = csv.writer(csvFile)

        # Loop over all SubTasks in the Configuration object and write them as rows to the file
        for config in configurations:
            for subTask in config.subTasks:
                writer.writerow([config.name, subTask.name, subTask.length])
        csvFile.close()

# Create a Configuration object based on an input CSV file
def loadConfigs(fileName):

    configDict = dict()
    # Open the csv file in read mode

    if os.path.exists(fileName):
        with open(fileName, "r") as csvFile:
            # Create csv reader object to read rows from csv file
            reader = csv.reader(csvFile)
            # Loop over the rows in the csv, assign first column to name variable and second column to length variable
            
            for rowIn in reader:
                configName = rowIn[0]
                subtaskName = rowIn[1]
                length = int(rowIn[2])

                config = configDict.get(configName)
                if config is None:
                    # Create the blank Configuration object, name is the input file name
                    config = Configuration.Configuration(configName)
                    configDict[configName] = config
                
                # Create SubTask object using name and length, add the SubTask object to Configuration object
                config.addSubTask(SubTask.SubTask(subtaskName, length))
            csvFile.close()
    return list(configDict.values())
