from math import exp
import numpy as np
import matplotlib.pyplot as plt

intialPopulation = 1000
birthRate = .3
deathRate = .1
pollutionNumber = 10
pollutionEffect = pollutionNumber/1000
intialPollution = 10
def changeInPollution(t, currentPollution):
    return 5 * t + currentPollution

def currentPopulationRate(pollutionEffect):
    return birthRate - deathRate - pollutionEffect

def newPopulation(currentPopulation, populationRate , changeInTime):
    return currentPopulation * (1 + populationRate) * changeInTime

def timeStep(currentPopulation, timeElapsed, currentPollution):
    pollutantEffect = changeInPollution(timeElapsed, currentPollution)
    populationRate = currentPopulationRate(currentPollution/100)
    newestPopulation = newPopulation(currentPopulation, populationRate, timeElapsed)
    if newestPopulation > 0:
        return newPopulation(currentPopulation, populationRate, timeElapsed)
    else:
        return 0

thisIsTheTimeStep = np.(1,16,1)
penguinPopulation = np.zeros(15)
previousPollution = np.zeros(15)
for i in range(len(thisIsTheTimeStep)):
    if i == 0:
        penguinPopulation[0] = intialPopulation
        previousPollution[0] = intialPollution
    else:    
        penguinPopulation[i] = timeStep(penguinPopulation[i-1],1,previousPollution[i-1])
        previousPollution[i] = changeInPollution(1,previousPollution[i-1])
    print(previousPollution[i])

plt.plot(thisIsTheTimeStep,penguinPopulation)

plt.show()