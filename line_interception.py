import matplotlib.pyplot as plt
import random

def generate_paths(xp,yp,vxp,vyp,zd,t):
    #get velocities for the drone to be at the same place as the platform at time t
    vxd = xp/t + vxp
    vyd = yp/t + vyp
    vzd = -zd/t
    #initiase lists for plotting
    plat_path = [[xp],[yp],[0]]
    drone_path = [[0],[0],[zd]]
    steps = 20
    dt = t/steps
    #simulate trajectory
    for s in range(steps):
        plat_path[0].append((plat_path[0][-1]+vxp*dt))
        plat_path[1].append((plat_path[1][-1]+vyp*dt))
        plat_path[2].append((plat_path[2][-1]))

        drone_path[0].append((drone_path[0][-1] + vxd * dt))
        drone_path[1].append((drone_path[1][-1] + vyd * dt))
        drone_path[2].append((drone_path[2][-1] + vzd * dt))
    print('total_velocity: {} m/s'.format((vxd**2+vyd**2+vzd**2)**0.5))
    return plat_path,drone_path

#initialise variables
#units are in meters,seconds or m/s²
xp = 0.7
yp = 0.7
vxp = 0.2
vyp = 0.1
zd = 1

ax = plt.axes(projection='3d')

#plot
for i in range(10):
    t = random.randint(3,14)
    platform,drone = generate_paths(xp,yp,vxp,vyp,zd,t)
    ax.plot(platform[0],platform[1],platform[2])
    ax.plot(drone[0],drone[1],drone[2])