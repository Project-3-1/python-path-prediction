import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()

ax = fig.add_subplot(aspect='equal')

data = pd.read_csv('Landing Experiments - Phase III - Sheet1.csv').dropna()

speeds = data['Platform Speed'].unique()
speeds.sort()

for speed in speeds:
    df = data[data['Platform Speed']==speed]
    avg = (sum((df['Landing Offset Y']**2+df['Landing Offset X']**2)**0.5/df.shape[0])*100)
    scat = ax.scatter(df['Landing Offset Y']*100, df['Landing Offset X']*100, label = str(speed))
    ax.add_artist(plt.Circle((0, 0), avg, color=scat.get_facecolors()[0].tolist(), fill = False, linestyle = '-.'))

ax.set_xlim(-27,27)
ax.set_ylim(-27,27) 


boxAr = plt.Rectangle((-13.2, -13.2), 26.4, 26.4,fill = False,ec="c")
boxPl = plt.Rectangle((-25, -25), 50, 50,fill = False,ec="r")
ax.add_artist(boxAr)
ax.add_artist(boxPl)

ax.text(-25,25.5,'Platform')
ax.text(-13.2,15,'ArUco marker')

ax.legend()
ax.grid(True)

plt.show()