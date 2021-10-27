import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.misc import derivative
from CoronaCrawler import CoronaCrawler

DRIVER_PATH = "res/chromedriver.exe"
crawler = CoronaCrawler(DRIVER_PATH)

data = crawler.getPortugalDailyTotalsData()

newInfected   = data[:, 0]
totalInfected = data[:, 1]
totalRecup    = data[:, 3]
totalDead     = data[:, 4]


plt.figure("Coronavírus in Portugal", figsize=(15, 7))
plt.subplot(2, 2, 1)
plt.plot(totalInfected)
plt.plot(totalRecup, 'g')
plt.plot(totalDead, 'r')
plt.yticks(np.arange(0, max(totalInfected), step=10000))
plt.xticks(np.arange(0, len(totalInfected), step=20))
plt.title("Coronavírus Predicted Progression in Portugal")
plt.ylabel("Nº of infected")
plt.xlabel("Days since infection started")
plt.grid()
blue_patch  = mpatches.Patch(color='blue',  label='Nº of Infected')
green_patch = mpatches.Patch(color='green', label='Nº of Recuperated')
red_patch   = mpatches.Patch(color='red',   label='Nº of Dead')
plt.legend(handles=[blue_patch, green_patch, red_patch])

plt.subplot(2, 2, 2)
plt.plot(newInfected)
# plt.yticks(np.arange(0, max(dailyInc[:,1]), step=100))
# plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
plt.yticks(np.arange(min(newInfected), max(newInfected), step=150))
plt.xticks(np.arange(0, len(newInfected), step=20))
plt.title("New Infection Cases")
plt.ylabel("Nº of new infected")
plt.xlabel("Days since infection started")
plt.grid()


plt.subplot(2, 2, 3)
plt.plot(totalDead, 'r')
# plt.yticks(np.arange(0, max(dailyInc[:,1]), step=100))
# plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
plt.yticks(np.arange(min(totalDead), max(totalDead), step=150))
plt.xticks(np.arange(0, len(totalDead), step=20))
plt.title("Total Dead")
plt.ylabel("Nº of deaths")
plt.xlabel("Days since infection started")
plt.grid()


plt.tight_layout()
plt.show()

















# def getInfectedByDay(infectProgressionFunc, day):
#    return infectProgressionFunc(day)
#
# def getDailyIncrement(infectedHistory):
#
#    dailyIncrements = np.zeros((infectedHistory.shape[0]-1, infectedHistory.shape[1]))
#
#    for i in range(1, len(infectedHistory)):
#       dailyIncrements[i-1] = (infectedHistory[i][0], infectedHistory[i][1] - infectedHistory[i-1][1])
#
#    return dailyIncrements









# dailyInc = getDailyIncrement(infectedHistory)
# print(dailyInc)
#
#
# # get x and y vectors
# x = infectedHistory[:, 0]
# y = infectedHistory[:, 1]
#
# # calculate polynomial
# coefs = np.polyfit(x, y, 4)  # Grau 4 ou 3
# infectProgressionFunc = np.poly1d(coefs)
#
# leftBound  = 2
# rightBound = 90
#
# # calculate new x's and y's
# x_new = np.linspace(leftBound, rightBound, 50)
# y_new = infectProgressionFunc(x_new)
#
# def generateDerivValues(infectProgressionFunc, infectedHistory):
#    derivValues = infectedHistory.copy()
#
#    for i in range(len(infectedHistory)):
#       # derivValues[i] = (infectedHistory[i, 0], derivative(infectProgressionFunc, infectedHistory[i, 1]))
#       derivValues[i] = (infectedHistory[i, 0], derivative(infectProgressionFunc, infectedHistory[i, 1]))
#
#    return derivValues
#
# print(getInfectedByDay(infectProgressionFunc, 32))
#
# # plt.figure(3, figsize=(15, 15))
#
#
# plt.figure("Coronavírus in Portugal", figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'o', x_new, y_new)
# plt.ylim([0,  max(max(y), max(y_new)) + 1000])
# plt.xlim([leftBound, rightBound])
# plt.yticks(np.arange(0, max(y_new), step=2000))
# plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
# plt.title("Coronavírus Predicted Progression in Portugal")
# plt.ylabel("Nº of infected")
# plt.xlabel("Days since infection started")
# plt.grid()
#
# plt.subplot(1, 2, 2)
# plt.plot(dailyInc[:, 0], dailyInc[:, 1], "C1")
#
# # print(dailyInc[0][0])
# plt.yticks(np.arange(0, max(dailyInc[:,1]), step=100))
# plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
# plt.title("New Infection Cases")
# plt.ylabel("Nº of new infected")
# plt.xlabel("Days since infection started")
# plt.grid()
#
# plt.tight_layout()
# plt.show()