import Meeting

# create unit test to test class Meeting
def testConstructor():
    testMeeting = Meeting.Meeting("test", "test", 1)
    assert testMeeting.name == "test" and testMeeting.password == "test" and testMeeting.duration == 1
    
def testConstructor():
    testMeeting = Meeting.Meeting("Google Interview", "google", 1)
    assert testMeeting.name == "Google Interview" and testMeeting.password == "google" and testMeeting.duration == 1
    
def testSetters():
    testMeeting = Meeting.Meeting("test", "test", 1)
    testMeeting.name = "test2"
    testMeeting.password = "test2"
    testMeeting.duration = 2
    assert testMeeting.name == "test2" and testMeeting.password == "test2" and testMeeting.duration == 2
    
def testSetters():
    testMeeting = Meeting.Meeting("test", "test", 1)
    testMeeting.name = "Interview"
    testMeeting.password = "password"
    testMeeting.duration = 2
    assert testMeeting.name == "Interview" and testMeeting.password == "password" and testMeeting.duration == 2    

def testStr():
    testMeeting = Meeting.Meeting("test", "test", 1)
    assert str(testMeeting) == "test - 1 seconds"
