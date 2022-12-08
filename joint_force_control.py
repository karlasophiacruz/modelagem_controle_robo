import time
import json
import os
from zmqRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

path_solid_simple = os.getcwd() + os.sep + 'solid_simple.ttt'
sim.loadScene(path_solid_simple)

joint1 = sim.getObject('/theta1')
joint2 = sim.getObject('/theta2')
joint3 = sim.getObject('/theta3')
joint4 = sim.getObject('/theta4')
joint5 = sim.getObject('/theta5')

client.setStepping(True)

sim.startSimulation()
data_f = open('data.txt', 'w+', encoding="utf-8")

data = []
forces1 = []
forces2 = []
forces3 = []
forces4 = []
forces5 = []

while (t := sim.getSimulationTime()) < 1:
    if((t := sim.getSimulationTime()) >= 0.04):
      force_joint1 = sim.getJointForce(joint1)
      forces1.append(force_joint1)

      force_joint2 = sim.getJointForce(joint2)
      forces2.append(force_joint2)

      force_joint3 = sim.getJointForce(joint3)
      forces3.append(force_joint3)

      force_joint4 = sim.getJointForce(joint4)
      forces4.append(force_joint4)

      force_joint5 = sim.getJointForce(joint5)
      forces5.append(force_joint5)

    time.sleep(0.05)
    client.step()

data.append(forces1)
data.append(forces2)
data.append(forces3)
data.append(forces4)
data.append(forces5)
json.dump(data, data_f)
data_f.close()

sim.stopSimulation()
print('program ended')

while(sim.getSimulationState() != sim.simulation_stopped):
  client.step()

#  setting joint forces

path_solid_force = os.getcwd() + os.sep + 'solid_force.ttt'
sim.loadScene(path_solid_force)

sim.startSimulation()

with open('data.txt', 'r') as f:
  data = json.load(f)
# print(data)

while (t := sim.getSimulationTime()) < 1:
    if((t := sim.getSimulationTime()) >= 0.04):
      # joint1
      force_joint1 = data[0].pop(0)

      # sim.setJointForce(joint1, 0)
      # sim.setJointForce(joint2, -0.18955104053020477)
      # sim.setJointForce(joint3, -0.1895412653684616)
      # sim.setJointForce(joint4, 0)
      # sim.setJointForce(joint5, 0)
      if(force_joint1 < 0):
        sim.setJointForce(joint1, -force_joint1)
      else:
        sim.setJointForce(joint1, force_joint1)

      # joint2
      force_joint2 = data[1].pop(0)

      if(force_joint2 < 0):
        sim.setJointForce(joint2, -force_joint2)
      else:
        sim.setJointForce(joint2, force_joint2)

      # joint3
      force_joint3 = data[2].pop(0)

      if(force_joint3 < 0):
        sim.setJointForce(joint3, -force_joint3)
      else:
          sim.setJointForce(joint3, force_joint3)

      # joint4
      force_joint4 = data[3].pop(0)

      if(force_joint4 < 0):
        sim.setJointForce(joint4, -force_joint4)
      else:
        sim.setJointForce(joint4, force_joint4)

      # joint5
      force_joint5 = data[4].pop(0)

      if(force_joint5 < 0):
        sim.setJointForce(joint5, -force_joint5)
      else:
        sim.setJointForce(joint5, force_joint5)

    time.sleep(0.05)
    client.step()

sim.stopSimulation()
print('program ended')

while(sim.getSimulationState() != sim.simulation_stopped):
  client.step()