#Import of needed modules
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
from math import pi, atan2
#Visualize 
import matplotlib.pyplot as plt
import numpy as np

#Create the robot model(Vehicle)
anim = VehicleIcon('rob.png', scale = 2)
#Initializing positions of robot
initx = float(input("Enter the X coordinate for the robot's initial position: "))
inity = float(input("Enter the Y coordinate for the robot's initial position: "))
initu=initialPos=[initx, inity]
veh = Bicycle(
    animation = anim,
    control = RandomPath,
    dim = 10,
    x0=(initialPos[0],initialPos[1],0),
)
#plot map obstacles and goal
veh.init(plot=True)
obs = int(input("Enter the number of obstacles: "))
map = LandmarkMap(obs, 20)
goal_x = float(input("Please input initial X coordinate for goal: "))
goal_y = float(input("Please input initial Y coordinate for goal: "))
goal = [goal_x, goal_y]
goal_marker_style = {
    'marker': 'D',
    'markersize': 6,
    'color': 'b',
}
plt.plot(goal[0], goal[1], **goal_marker_style)
map.plot()
# Range bearing sensor
sensor=RangeBearingSensor(robot=veh,map=map, animate=True)
for i in sensor.h(veh.x):
    dis_land = i[0]
    ang_land = i[1]

# inserting goal inside array(append)

goal_array=[goal]
goal_array.append(goal)
goal_array.insert(0,initialPos)
x_array=[item[0] for item in goal_array]
y_array=[item[1] for item in goal_array]

s_s = pi/4
#loop
run=True
target=[goal_array]
while(run):
    for i in sensor.h(veh.x):
        if (i[0] > 0.5) and (abs(i[1]) > s_s/2):
            goal_heading = atan2(
                goal[1] - veh.x[1],
                goal[0] - veh.x[0]
                )
            steer = goal_heading-veh.x[2]
            plt.pause(0.005)
        else:
            veh.step(-1,0)
            plt.pause(0.005)
        veh._animation.update(veh.x)
#plot graph
plt.plot(goal[0], goal[1], **goal_marker_style)