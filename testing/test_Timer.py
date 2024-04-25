# Run tests using "python -m pytest" in command line pointing to parent directory
import time
import Timer
from SoundManager import SoundManager

soundManagerTesting = SoundManager()
soundManagerTesting.enabled = False

def testCountDown(capfd):
    duration = 3
    timer = Timer.Timer(duration, soundManagerTesting)
    timer.showTimer = lambda time: None

    expectedEndTime = time.time() + duration + 1
    timer.countDown()
    actualEndTime = time.time()
    assert(expectedEndTime >= actualEndTime - 1)
    assert(expectedEndTime <= actualEndTime + 1)

    out,err = capfd.readouterr()
    assert out.strip()=="Time is up!"

def testTick(capfd):
    timer = Timer.Timer(30, soundManagerTesting)
    timer.waitOneSecond = lambda: None

    for i in range(30, 0, -1):
        timer.tick()

        out,err = capfd.readouterr()
        if i >= 10:
            assert out.strip()=="00:" + str(i)
        else:
            assert out.strip()=="00:0" + str(i)

def testPause(capfd):
    timer = Timer.Timer(30, soundManagerTesting)
    timer.waitOneSecond = lambda: None
    timer.fetchInput = lambda: None

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:30"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:29"

    timer.fetchInput = lambda: "p"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:28"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:28"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:28"
    
    timer.fetchInput = lambda: "r"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:28"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:27"
    
def testAdvance(capfd):
    timer = Timer.Timer(30, soundManagerTesting)
    timer.waitOneSecond = lambda: None
    timer.fetchInput = lambda: None

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:30"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:29"

    timer.fetchInput = lambda: "a"

    timer.tick() 
    out,err = capfd.readouterr()
    assert out.strip()=="00:28"

    timer.countDown()
    out,err = capfd.readouterr()
    assert out.strip()=="Time is up!"

def testProperties():
    timer = Timer.Timer(30, soundManagerTesting)
    assert timer.duration==30
    timer.duration = 20
    assert timer.duration==20
