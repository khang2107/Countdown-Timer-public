# Run tests using "python -m pytest" in command line pointing to parent directory
import Configuration
import SubTask

#Test constructor works correctly
def testConstructor():
    
    #Create new Configuration object with name "test"
    testConfig = Configuration.Configuration("test")

    #Assert the name is "test" and the subTasks array is empty
    assert testConfig.name == "test" and testConfig.subTasks == []

#Test name setter works correctly
def testNameSetter():
    testConfig = Configuration.Configuration("test")

    #Change name of Configuration object and assert the change has occurred
    testConfig.name = "newTest"
    assert testConfig.name == "newTest"

#Test function for adding sub tasks works correctly
def testAddSubTask():
    testConfig = Configuration.Configuration("test")

    #Create new SubTask object, add it to the Configuration object, and assert it was added correctly
    subTaskIn = SubTask.SubTask("task1", 2)
    testConfig.addSubTask(subTaskIn)
    assert testConfig.subTasks == [subTaskIn]

#Test function for removing sub tasks works correctly
def testRemoveSubTask():
    testConfig = Configuration.Configuration("test")
    subTaskIn = SubTask.SubTask("task1", 2)
    testConfig.addSubTask(subTaskIn)

    #Read the SubTask into a variable, remove that SubTask object and assert it was removed
    removeSubTask = testConfig.subTasks[0]
    testConfig.removeSubTask(removeSubTask)
    assert testConfig.subTasks == []