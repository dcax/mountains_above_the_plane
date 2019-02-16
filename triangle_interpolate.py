import numpy as np
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator


class TriangularInterpolation:
    #This creates an interpolation from file
    def __init__(self, points):
        #Read from file
        #assume points is an array of dicts
        points = np.array([[p['x'],p['y']] for p in points])
        self.tri = Delaunay(points)

        
    
    def lift_points(self, hs, xs, ys):
        #point should be within the triangular mesh
        #points = np.array(points)
        values = np.array(values) #This takes array to np array
        #Values should always be in order of the points which are added.
        self.interpolator = LinearNDInterpolator(values=values, points=self.tri)

    def interpolate(self, values):
        
        
        results = self.interpolator.call(values)
        #Some values may be NaN
        return results

        """simplex = self.tri.find_simplex()
        if simplex == -1:
            #outside of triangular mesh
            pass
        """


        