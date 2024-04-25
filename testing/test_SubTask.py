# Run tests using "python -m pytest" in command line pointing to parent directory
import SubTask

def testConstructor():
    testSubTask = SubTask.SubTask("test", 1)
    assert testSubTask.name == "test" and testSubTask.length == 1

def testSetters():
    testSubTask = SubTask.SubTask("test", 1)
    testSubTask.name = "test2"
    testSubTask.length = 2
    assert testSubTask.name == "test2" and testSubTask.length == 2