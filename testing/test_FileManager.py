# Run tests using "python -m pytest" in command line pointing to parent directory
import FileManager
import Configuration
import SubTask

def testOutputInput():
    testConfig = Configuration.Configuration("test")
    testSubTask = SubTask.SubTask("task1", 1)
    testSubTask2 = SubTask.SubTask("task2", 2)
    testConfig.addSubTask(testSubTask)
    testConfig.addSubTask(testSubTask2)
    FileManager.outputConfig(testConfig)

    testConfigIn = FileManager.inputConfig("test")
    assert testConfigIn.name == "test"
    assert testConfigIn.subTasks[0].name == "task1"
    assert testConfigIn.subTasks[0].length == 1
    assert testConfigIn.subTasks[1].name == "task2"
    assert testConfigIn.subTasks[1].length == 2