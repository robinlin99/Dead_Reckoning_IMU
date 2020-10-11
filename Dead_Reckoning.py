import numpy.matlib 
import numpy as np 
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot
import matplotlib.animation as animation
 
'''
Python-based dead reckoning algorithm for inertial navigation system
System Input:
	- Accelerometer Data
	- Gyroscope Data
	- Euler Angle
'''

def sin(x):
	return math.sin(x)

def cos(x):
	return math.cos(x)

class Dead_Reckoning():
		def __init__(self, localAcc, localAngular, resolution, steps):
			# Raw data from accelerometer and gyroscope
			self.raw_acc = localAcc
			self.raw_ang_vel = localAngular
			self.delta_t = resolution
			self.steps = steps
			self.localAcc = localAcc
			self.globalVec = [np.array([[0],
                          		   	    [0],
                                   	    [0]])]
			self.globalPos = [np.array([[0],
                          		   		[0],
                                   		[0]])]
			self.angles = [np.array([[0],
                          		     [0],
                                     [0]])]
			# Initially, it is an identity matrix
			self.rotation_matrix = np.array([[1,0,0],
                          		   			 [0,1,0],
                                             [0,0,1]])
			g = 9.81
			self.gravity = np.array([[0],
                          		     [0],
                                     [-1*g]])
			self.x = [0]
			self.y = [0]
			self.z = [0]
			self.xhat = [np.array([[0.00001],
                          		   [0],
                                   [0]])]

			self.yhat = [np.array([[0],
                          		   [0.00001],
                                   [0]])]

			self.zhat = [np.array([[0],
                          		   [0],
                                   [0.00001]])]
		def simulate(self):
			for i in range(self.steps):
				print("Step #: " + str(i))
				angle_delta = self.raw_ang_vel[i] * self.delta_t

				C = float(angle_delta[2])
				B = float(angle_delta[1])
				A = float(angle_delta[0])

				rotation = np.array([[cos(C)*cos(B),-1*sin(C)*cos(A) + cos(C)*sin(B)*sin(A), sin(C)*sin(A) + cos(C)*sin(B)*cos(A)],
                          		     [sin(C)*cos(B), cos(C)*cos(A) + sin(C)*sin(B)*sin(A), -1*cos(C)*sin(A) + sin(C)*sin(B)*cos(A)],
                                     [-1*sin(B), cos(B)*sin(A), cos(B)*cos(A)]]) 


				self.rotation_matrix = np.matmul(self.rotation_matrix,rotation)
				
				new_global_acc = self.rotation_matrix.dot(self.localAcc[i]) - self.gravity	
				print('Accel')
				print(new_global_acc)
				
				
				new_global_vel = self.globalVec[-1] + self.delta_t * new_global_acc
				self.globalVec.append(new_global_vel)
				print("Vel")
				print(new_global_vel)

				
				new_global_pos = self.globalPos[-1] + self.delta_t * new_global_vel
				self.globalPos.append(new_global_pos)

				self.x.append(float(new_global_pos[0]))
				self.y.append(float(new_global_pos[1]))
				self.z.append(float(new_global_pos[2]))

				print("X: " + str(float(new_global_pos[0])))
				print("Y: " + str(float(new_global_pos[1])))
				print("Z: " + str(float(new_global_pos[2])))

				new_xhat = np.matmul(self.rotation_matrix,np.array([[1],
                          		   							    	[0],
                                   									[0]]))

				new_yhat = np.matmul(self.rotation_matrix,np.array([[0],
                          		   									[1],
                                   									[0]]))

				new_zhat = np.matmul(self.rotation_matrix,np.array([[0],
                          		   									[0],
                                   									[1]]))

				self.xhat.append(new_xhat)
				self.yhat.append(new_yhat)
				self.zhat.append(new_zhat)

				print("X-Hat")
				print(new_xhat)
				print("Y-Hat")
				print(new_yhat)
				print("Z-Hat")
				print(new_zhat)
			
		def plot_traj(self):
			fig = pyplot.figure()
			ax = Axes3D(fig)
			ax.set_xlabel('$X$')
			ax.set_ylabel('$Y$')
			ax.set_zlabel('$Z$')
			ax.scatter(self.x, self.y, self.z,s=[0.03]*len(self.x))
			pyplot.show()






