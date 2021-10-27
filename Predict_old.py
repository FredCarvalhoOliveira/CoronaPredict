import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

def getInfectedByDay(infectProgressionFunc, day):
   return infectProgressionFunc(day)

def getDailyIncrement(infectedHistory):

   dailyIncrements = np.zeros((infectedHistory.shape[0]-1, infectedHistory.shape[1]))

   for i in range(1, len(infectedHistory)):
      dailyIncrements[i-1] = (infectedHistory[i][0], infectedHistory[i][1] - infectedHistory[i-1][1])

   return dailyIncrements

# NOTAS:
# Periodo de quarentena 15 dias
# Estado de emergência 18 de Março
infectedHistory = np.array([(2, 2),      (3, 4),      (4, 6),
                            (5, 9),      (6, 13),     (7, 21),
                            (8, 30),     (9, 39),     (10, 41),
                            (11, 59),    (12, 78),    (13, 112),
                            (14, 169),   (15, 245),   (16, 331),
                            (17, 448),   (18, 642),   (19, 785),
                            (20, 1020),  (21, 1280),  (22, 1600),
                            (23, 2060),  (24, 2362),  (25, 2995),
                            (26, 3544),  (27, 4268),  (28, 5170),
                            (29, 5962),  (30, 6408),  (31, 7443),
                            (32, 8251),  (33, 9034),  (34, 9886),
                            (35, 10524), (36, 11278), (37, 11730),
                            (38, 12442), (39, 13141), (40, 13956),
                            (41, 15472), (42, 15987), (43, 16585),
                            (44, 16934), (45, 17448), (46, 18091),
                            (47, 18841), (48, 19022), (49, 19685),
                            (50, 20206), (51, 20863), (52, 21379),
                            (53, 21982), (54, 22353), (55, 22797),
                            (56, 23392), (57, 23864), (58, 24027),
                            (59, 24322), (60, 24505), (61, 25056),
                            (62, 25351), (63, 25190), (64, 25282),
                            (65, 25524), (66, 25702), (67, 26182),
                            (68, 26715), (69, 27268), (70, 27406),
                            (71, 27581), (81, 29660)]) ## UPDATE VALUES TO RECENT EVENTS

dailyInc = getDailyIncrement(infectedHistory)
print(dailyInc)


# get x and y vectors
x = infectedHistory[:, 0]
y = infectedHistory[:, 1]

# calculate polynomial
coefs = np.polyfit(x, y, 4)  # Grau 4 ou 3
infectProgressionFunc = np.poly1d(coefs)

leftBound  = 2
rightBound = 90

# calculate new x's and y's
x_new = np.linspace(leftBound, rightBound, 50)
y_new = infectProgressionFunc(x_new)

def generateDerivValues(infectProgressionFunc, infectedHistory):
   derivValues = infectedHistory.copy()

   for i in range(len(infectedHistory)):
      # derivValues[i] = (infectedHistory[i, 0], derivative(infectProgressionFunc, infectedHistory[i, 1]))
      derivValues[i] = (infectedHistory[i, 0], derivative(infectProgressionFunc, infectedHistory[i, 1]))

   return derivValues

print(getInfectedByDay(infectProgressionFunc, 32))

# plt.figure(3, figsize=(15, 15))


plt.figure("Coronavírus in Portugal", figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'o', x_new, y_new)
plt.ylim([0,  max(max(y), max(y_new)) + 1000])
plt.xlim([leftBound, rightBound])
plt.yticks(np.arange(0, max(y_new), step=2000))
plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
plt.title("Coronavírus Predicted Progression in Portugal")
plt.ylabel("Nº of infected")
plt.xlabel("Days since infection started")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(dailyInc[:, 0], dailyInc[:, 1], "C1")

# print(dailyInc[0][0])
plt.yticks(np.arange(0, max(dailyInc[:,1]), step=100))
plt.xticks(np.arange(0, x_new[-1] + 2, step=5))
plt.title("New Infection Cases")
plt.ylabel("Nº of new infected")
plt.xlabel("Days since infection started")
plt.grid()

plt.tight_layout()
plt.show()