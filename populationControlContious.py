from math import exp
import numpy as np
import matplotlib.pyplot as plt

global currentPollution, cleanedPollution
cleanedPollution = 0
currentPollution = 10
pollutionRate = 5
intialPopulation = 1000
birthRate = .3
deathRate = .1




def currentPopulation(timeElapsed):
    currentPollution = pollutionRate * timeElapsed - cleanedPollution 
    pollutionEffect = currentPollution/100
    populationRate = 1 + birthRate - deathRate - pollutionEffect
    return intialPopulation*exp(populationRate * timeElapsed)

print(currentPopulation(5))