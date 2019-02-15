#!/bin/env python3

#This ode is meant to run and create the triangular mappings used for linear interpolation of points in temp and etc.


#INPUTS: loc.csv
#OUTPUTS: triangles.csv

import matplotlib.pyplot as plt #REMOVE THIS AT RUN; Unneccessay

import pandas as pd
import numpy as np
from pprint import pprint
#Uses Delaunay triangulation for efficiency
#and optimal triangle choice
input_csv_file = "locs.csv"
output_file = "triangles.csv"

locs = pd.read_csv(input_csv_file,delimiter=',')
#Name col is not used at the moment
print(locs)

points = locs[['x','y']].values #np.asarray(locs[['x','y']]) 
#turns pandas "spreadsheet" into array of numpy x,y tuples
points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])


pprint(points)
from scipy.spatial import Delaunay 
triangulation = Delaunay(points)
print("Tri created.")


plt.triplot(points[:,0],points[:,1], triangulation.simplices.copy())
plt.plot(points[:,0],points[:,1], 'o')
plt.show()



