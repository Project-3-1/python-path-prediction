from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
import csv
import matplotlib.animation as manimation
fig = plt.figure()
ax = p3.Axes3D(fig)

times = []
x_line = []
y_line = []
z_line = []

#rostopic echo -b file.bag -p /topic
# ["range.front", "range.right", "range.back", "range.left", "range.up"]
with open('success_07.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        line_count += 1
        times.append(float(row['field.header.stamp']) * 0.000000001)
        x_line.append(float(row['field.pose.position.x']))
        y_line.append(float(row['field.pose.position.y']))
        z_line.append(float(row['field.pose.position.z']))
print(line_count)
x_line = np.array(x_line)
y_line = np.array(y_line)
z_line = np.array(z_line)
times = np.array(times)

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

N = len(x_line)
print(((times[-1]-times[0])/N))
data = np.array([x_line,y_line,z_line])
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([min(x_line) - 0.2, max(x_line) + 0.2])
ax.set_xlabel('X [m]')

ax.set_ylim3d([min(y_line) - 0.2, max(y_line) + 0.2])
ax.set_ylabel('Y [m]')

ax.set_zlim3d([min(z_line) - 0.2, max(z_line) + 0.2])
ax.set_zlabel('Z [m]')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1000*((times[-1]-times[0])/N), blit=False)
ani.save('demo_flight.mp4', writer='ffmpeg', dpi=300)
plt.show()

