import numpy as np

def prizeDoor(nsim):
    return np.random.randint(0,3,nsim)

def chooseDoor(nsim):
    return np.random.randint(0,3,nsim)

def goatDoor(initialGuesses,prizeDoors):
    result = np.random.randint(0,3,prizeDoors.size)
    while True:
        bad = (result==prizeDoors)|(result==initialGuesses)
        if not bad.any():
            return result
        result[bad]=np.random.randint(0,3,bad.sum())

def switchGuess(initialGuesses,goatDoors):
    result=np.zeros(initialGuesses.size)
    switch={(0,1):2, (0,2):1, (1,0):2, (1,2):0, (2,0):1, (2,1):0}
    for i in [0,1,2]:
        for j in [0,1,2]:
            mask = (initialGuesses==i) & (goatDoors==j)
            if not mask.any():
                continue
            result = np.where(mask,np.ones_like(result)*switch[(i,j)],result)
    return result

    
def win_percentage(guesses,prizeDoors):
    return sum(guesses==prizeDoors)/float(prizeDoors.size)*100


nsim=10000
prizeDoors = prizeDoor(nsim)
initialGuesses = chooseDoor(nsim)
goatDoors = goatDoor(initialGuesses,prizeDoors)
switchedGuesses = switchGuess(initialGuesses,goatDoors)

print "Win percentage without switching: " + str(win_percentage(initialGuesses,prizeDoors))

print "Win percentage when switching: " + str(win_percentage(switchedGuesses,prizeDoors))
