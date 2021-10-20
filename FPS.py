import time as t


def fps(pTime):
    cTime = t.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    return fps, pTime
