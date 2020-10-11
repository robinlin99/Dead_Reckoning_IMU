import Dead_Reckoning
import numpy.matlib 
import numpy as np 
import math
from mpl_toolkits import mplot3d

if __name__ == "__main__": 
	'''
	Init: localAcc, localAngular, resolution, steps
	'''
	resolution = 0.0001

	acc1 = [np.array([[4],
                     [0],
                     [-9.81]])] * 500
	acc2 = [np.array([[-4],
                     [0],
                     [-9.81]])] * 500
	acc3 = [np.array([[0],
                     [4],
                     [-9.81]])] * 500
	acc4 = [np.array([[0],
                     [-4],
                     [-9.81]])] * 500
	acc5 = [np.array([[-4],
                     [0],
                     [-9.81]])] * 500

	acc6 = [np.array([[4],
                     [0],
                     [-9.81]])] * 500

	acc7 = [np.array([[0],
                     [-4],
                     [-9.81]])] * 500

	acc8 = [np.array([[0],
                     [4],
                     [-9.81]])] * 500

	acc9 = [np.array([[0],
                     [0],
                     [-8.9]])] * 500



	acc = acc1 + acc2 + acc3 + acc4 + acc5 + acc6 + acc7 + acc8 + acc9
	localAngular = [np.array([[0],
                             [0.003],
                             [0]])] * len(acc)
	steps = len(acc)
	new_sim = Dead_Reckoning.Dead_Reckoning(acc,localAngular,resolution,steps)
	new_sim.simulate()
	new_sim.plot_traj()