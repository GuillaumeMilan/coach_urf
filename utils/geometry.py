import numpy as np
def intersec(a,b,a_p,b_p):
    denom = (a["x"]-b["x"])*(a_p["y"]-b_p["y"]) - (a["y"]-b["y"])*(a_p["x"]-b_p["x"])
    num = (a_p["y"]-a["y"])*(a_p["x"]-b_p["x"]) - (a_p["x"]-a["x"])*(a_p["y"]-b_p["y"])

    return num/denom

class Point:
    def __init__(self, first = None, x = None, y = None):
        if type(first) == Point:
            self.data = first.data
            return
        if type(first) == type({}):
            self.data = first
            return
        if x and y:
            self.data = {"x": x, "y": y}
            return
        #raise Exception("Need coordinate to initialize a point")
        self.data = {"x": 0, "y": 0}
        return
    def __getitem__(self, name):
        return self.data[name]
    def __setitem__(self, name, value):
        self.data[name] = value
        return
    def __add__(self, point):
        return Point({"x": self.data["x"] + point.data["x"], "y": self.data["y"] + point.data["y"]})
    def __sub__(self, point):
        return Point({"x": self.data["x"] - point.data["x"], "y": self.data["y"] - point.data["y"]})
    def __mul__(self, coef):
        return Point({"x": coef*self.data["x"], "y": coef*self.data["y"]})
    def aligned(points):
        if len(points<3):
            return True
        ref_a = points[0]
        ref_b = points[1]
        direction = ref_b - ref_a
        for p in points[2:]:




def Line:
    def __init__(self, points):
        self.aligned(points)
        self._points = points

    def getRef(index):
        if index = 

    def intersect(line):
        denom = (self._a["x"]-self._b["x"])*(a_p["y"]-b_p["y"]) - (a["y"]-b["y"])*(a_p["x"]-b_p["x"])
        num = (a_p["y"]-a["y"])*(a_p["x"]-b_p["x"]) - (a_p["x"]-a["x"])*(a_p["y"]-b_p["y"])

class Rectangle()
