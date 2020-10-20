import numpy as np 
import csv
#'./B_Accelerometer_data/jog_9/sub_3.csv'
#'./C_Gyroscope_data/jog_9/sub_3.csv'
def extract(filepath,type):
	f = open(filepath)
	csv_f = csv.reader(f)
	data = []
	for i,row in enumerate(csv_f):
		if i > 0:
			xdata = float(row[1])
			ydata = float(row[2])
			zdata = float(row[3])
			print(xdata, ydata, zdata)
			if type == "acc":
				data.append(np.array([[xdata],
					[ydata],
					[zdata-9.81]]))
			else:
				data.append(np.array([[xdata],
					[ydata],
					[zdata]]))

	return data
