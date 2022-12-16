import numpy as np
import math
import roboticstoolbox as rtb
import matplotlib.pyplot as plt
def MT01(theta0):
  mat = [[math.cos(theta0), 0, -math.sin(theta0), 0],
         [math.sin(theta0), 0, math.cos(theta0), 0],
         [0, -1, 0, 0.11],
         [0,  0,  0, 1]]
  
  return np.array(mat)

def MT12(theta1):
  mat = [[math.cos(theta1-(math.pi/2)),-math.sin(theta1-(math.pi/2)), 0, 0.125*math.cos(theta1-(math.pi/2))],
         [math.sin(theta1-(math.pi/2)), math.cos(theta1-(math.pi/2)), 0, 0.125*math.sin(theta1-(math.pi/2))],
         [0, 0, 1, 0],
         [0,  0,  0, 1]]
  
  return np.array(mat)

def MT23(theta2):
  mat = [[math.cos(theta2+(math.pi/2)),-math.sin(theta2+(math.pi/2)), 0, 0.096*math.cos(theta2+(math.pi/2))],
         [math.sin(theta2+(math.pi/2)), math.cos(theta2+(math.pi/2)), 0, 0.096*math.sin(theta2+(math.pi/2))],
         [0, 0, 1, 0],
         [0,  0,  0, 1]]
  
  return np.array(mat)

def MT34(theta3):
  mat = [[math.cos(theta3+(math.pi/2)), 0, math.sin(theta3+(math.pi/2)), 0.0275*math.cos(theta3+(math.pi/2))],
         [math.sin(theta3+(math.pi/2)), 0, -math.cos(theta3+(math.pi/2)), 0.0275*math.sin(theta3+(math.pi/2))],
         [0, 1, 0, 0],
         [0,  0,  0, 1]]
  
  return np.array(mat)

def MT45(theta):
  mat = [[math.cos(theta),-math.sin(theta), 0, 0],
         [math.sin(theta), math.cos(theta), 0, 0],
         [0, 0, 1, 0.065],
         [0,  0,  0, 1]]
  
  return np.array(mat)

def fkine(theta0, theta1, theta2, theta3, theta4):
    return MT01(theta0)@MT12(theta1)@MT23(theta2)@MT34(theta3)@MT45(theta4)
    
t01 = rtb.robot.DHLink(d=0.11, alpha = -math.pi/2)
t12 = rtb.robot.DHLink(a=0.125, offset = -math.pi/2)
t23 = rtb.robot.DHLink(a=0.096, offset = math.pi/2)
t34 = rtb.robot.DHLink(a= 0.0275, offset = math.pi/2, alpha = math.pi/2)
t45 = rtb.robot.DHLink(d=0.065)

dof5 = rtb.robot.DHRobot([t01, t12, t23, t34, t45], name = '5-DOF Arm')
q = [0, 0, 0, 0, 0]

dof5.plot(q, 'pyplot', block=True)

a_fkine_dof5 = fkine(q[0], q[1], q[2], q[3],  q[4])
b_fkine_dof5 = rtb.DHRobot.fkine(dof5, q)

print(a_fkine_dof5)
print(b_fkine_dof5)

