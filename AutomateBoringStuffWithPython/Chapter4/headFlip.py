import random

FLIPCOUNT = 100
STREAKCOUNT = 6
TRIALCOUNT = 10


def checkStreak(tossList,checkValue):
    count = 0
    streakCount = 0
    for i in range(0,len(tossList)):
        if tossList[i] == checkValue:
            count += 1
        else:
            if(count >= STREAKCOUNT):
                streakCount += 1
            count = 0
    if count >= STREAKCOUNT:
        streakCount += 1
    return streakCount

trial = 0
streakCount = 0
while trial < TRIALCOUNT:
    tosses = []
    for i in range(0,FLIPCOUNT):
        tosses.append(random.randint(0,1))
    streakCount += checkStreak(tosses,0)
    streakCount += checkStreak(tosses,1)

    trial += 1
print('Streak Count: ' + str(streakCount))

