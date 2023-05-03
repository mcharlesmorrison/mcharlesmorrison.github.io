import numpy as np
import matplotlib.pyplot as plt

# seattube/head tube angle change through travel
travel = 120
hta = 65
sFork = np.linspace(1, 140, 140)
sag = 140 * 0.175
totalVert = travel * np.sin(np.deg2rad(hta))
totalAngle = 6.1

staRange = np.linspace(80, 80+totalAngle, 140)
p = np.polyfit(sFork, staRange, 1)
staSag = p[0] * sag + p[1]

htaRange = np.linspace(65, 65+totalAngle, 140)
p = np.polyfit(sFork, htaRange, 1)
htaSag = p[0] * sag + p[1]

fig, axs = plt.subplots(2, 1, figsize=(8, 8))
fig.subplots_adjust(hspace=0.5)

axs[0].plot(sFork, staRange)
axs[0].grid(True, which='both', linestyle='--')
axs[0].scatter(sag, staSag)
axs[0].legend(['ST Angle', 'ST Angle @ Sag'], loc='upper left')
axs[0].set_title('Seattube Angle Through Travel')
axs[0].set_xlabel('fork displacement [mm]')
axs[0].set_ylabel('seattube angle [deg]')

axs[1].plot(sFork, htaRange)
axs[1].grid(True, which='both', linestyle='--')
axs[1].scatter(sag, htaSag)
axs[1].legend(['HT Angle', 'HT Angle @ Sag'], loc='upper left')
axs[1].set_title('Headtube Angle Through Travel')
axs[1].set_xlabel('fork displacement [mm]')
axs[1].set_ylabel('headtube angle [deg]')

plt.show()

