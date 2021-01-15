import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()

ax = fig.add_subplot(aspect='equal')

data = pd.read_csv('Landing Experiments - Phase III - Sheet1.csv').dropna()
val = [0,0.5,1] #values to plot
data = data[data['Platform Speed'].isin(val)]
speeds = data['Platform Speed'].unique()
speeds.sort()

for speed in speeds:
    df = data[data['Platform Speed']==speed]
    avg = (sum((df['Landing Offset Y']**2+df['Landing Offset X']**2)**0.5/df.shape[0])*100)
    scat = ax.scatter(df['Landing Offset Y']*100, df['Landing Offset X']*100, label = str(speed) + ' m/s')
    ax.add_artist(plt.Circle((0, 0), avg, color=scat.get_facecolors()[0].tolist(), fill = False, linestyle = '-.'))

ax.set_xlim(-27, 27)
ax.set_ylim(-27, 27) 


boxAr = plt.Rectangle((-13.2, -13.2), 26.4, 26.4, fill = False, ec="c")
boxPl = plt.Rectangle((-25, -25), 50, 50, fill = False, ec="r")
ax.add_artist(boxAr)
ax.add_artist(boxPl)

ax.text(-25,25.5,'Platform')
ax.text(-13.2,14,'ArUco marker')

ax.legend()
ax.grid(True)

total_dist = ((data['Landing Offset Y']**2+data['Landing Offset X']**2)**0.5)*100
total_dist = total_dist.to_list()
total_dist.sort()
# circles for top n %
#ax.add_artist(plt.Circle((0, 0), total_dist[int(0.5*len(total_dist))], fill = False, linestyle = '-'))
#ax.add_artist(plt.Circle((0, 0), total_dist[int(0.95*len(total_dist))], fill = False, linestyle = '-'))
#ax.add_artist(plt.Circle((0, 0), total_dist[int(0.05*len(total_dist))], fill = False, linestyle = '-'))

plt.show()

on_aruco = data[(abs(data['Landing Offset Y']*100) <= 13.2) & (abs(data['Landing Offset X']*100) <= 13.2)].shape[0]
print(on_aruco/data.shape[0])
