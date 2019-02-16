import numpy as np
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator


class TriangularInterpolation:
    #This creates an interpolation from file
    def __init__(self, points):
        #Read from file
        #assume points is an array of dicts
        #This convers it to np.array of arrays
        self.points = np.array([[p['x'],p['y']] for p in points])
        self.tri = Delaunay(self.points)

        
    
    def lift_points(self, hs, xs, ys):
        #point should be within the triangular mesh
        #points = np.array(points)
        self.values = np.array(values) #This takes array to np array
        #Values should always be in order of the points which are added.
        self.interpolator = LinearNDInterpolator(values=self.values, points=self.tri)

    def interpolate(self, points_of_intrest):
        
        
        results = self.interpolator.call(points_of_intrest)
        #Some values may be NaN
        return results

        """simplex = self.tri.find_simplex()
        if simplex == -1:
            #outside of triangular mesh
            pass
        """

    def dist(x,y):
        #computes simple distance over two points (2-tuples)
        return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

    def extrapolate(self, points_of_intrest):
        #assumes value is outside the mesh
        #This works over array for easy of use
        points_of_intrest = np.array([[p['x'],p['y']] for p in points_of_intrest])
        closest_points = []
        r = []
        for p in points_of_intrest:
            #we could do a linear search because we don't know 
            # if points is ordered
            distances = np.apply_along_axis(lambda point: dist(point,p), 0, self.points)
            #this basically uses map to create an array of dists
            min_distance = distances[0]
            min_index = 0
            for index, dist in np.ndenumerate(distances):
                if dist <= min_distance:
                    min_distance = dist #classical min finding
                    min_index = index
            closest_points.append(self.points[min_index])
            r.append(self.values[min_index])

        return r



   