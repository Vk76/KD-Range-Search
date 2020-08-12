# imports

import matplotlib.pyplot as plt
import math


class TwoDimensionRangeSearch:
    def __init__(self):
        self.points = []
        plt.rcParams["figure.figsize"] = [6, 6]
        self.left = float('inf')
        self.right = -float('inf')
        self.up = -float('inf')
        self.down = float('inf')

    def add(self, points):
        """
        params:
            points : tuple of (x,y)
        funtions:
            adds points or point to the points list
        """
        if type(points) == type(()):
            self.points.append(points)

        if type(points) == type([]):
            self.points.extend(points)
        # print(points)
        self.left = math.floor((min(self.points))[0])-1
        self.right = math.ceil((max(self.points))[0])+1
        self.down = math.floor((min(self.points, key=lambda x: x[1]))[1])-1
        self.up = math.ceil((max(self.points, key=lambda x: x[1]))[1])+1

    def drawPoints(self):
        """
        funtions:
            scatter and plot points 
        """
        for x, y in self.points:
            plt.scatter(x, y)

    def query(self, point):
        """
        params:
            point: tuple of (x,y)
        funtions:
            returns the number of iterations and status of the input point in O(log(n))
        """
        vertical = True
        iterations, found = self.findPoint(
            point, vertical, self.points, self.left, self.down, self.right, self.up)
        title = 'Searching for point ('+str(point[0])+','+str(
            point[1])+')'+'\nPoint'+[' not', ''][found] + ' found'
        plt.title(title)
        plt.grid()
        plt.show()
        return iterations, found

    def findPoint(self, point, vertical, points, left, down, right, up):
        """
        params:
            point : tuple of (x,y)
            vertical : boolean , if vertical split or horizontal
            points : list of left points
            left : left boundary
            right : right boundary
            down : down boundary
            up : up boundary

        funtions:
            recursive functions that split the area into vertical or horizontal 
        """

        if not vertical:

            vertical = True
            mid = len(points)//2
            mid += -1 if mid % 2 == 0 and mid != 0 else 0

            points = sorted(points, key=lambda x: x[1])
            plt.plot([left, right], [
                     points[mid][1], points[mid][1]], color='b')

            if point == points[mid]:
                return 1, True
            elif mid == 0:
                return 0, False
            elif point[1] > points[mid][1]:
                itr, got = self.findPoint(
                    point, vertical, points[mid+1:len(points)], left, points[mid][1], right, up)
                return itr+1, got
            else:
                itr, got = self.findPoint(
                    point, vertical, points[:mid], left, down, right,  points[mid][1])
                return itr+1, got
        else:
            vertical = False
            mid = len(points)//2
            mid += -1 if mid % 2 == 0 and mid != 0 else 0

            points = sorted(points)
            plt.plot([points[mid][0], points[mid][0]], [
                     down, up], color='g')

            if point == points[mid]:
                return 1, True
            elif mid == 0:
                return 0, False
            elif point[0] > points[mid][0]:
                itr, got = self.findPoint(
                    point, vertical, points[mid+1:len(points)], points[mid][0], down, right,  up)
                return itr+1, got
            else:
                itr, got = self.findPoint(
                    point, vertical, points[:mid], left, down, points[mid][0], up)
                return itr+1, got
