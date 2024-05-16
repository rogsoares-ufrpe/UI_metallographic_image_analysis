# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:23:07 2024

@author: roger
"""

from sympy import Point, Circle, Line


p1, p2 = Point(1/2, 2), Point(2,2)
l1 = Line(p1, p2)

Center = Point(2,2)

c1 = Circle(Center, 1)

inter = c1.intersection(l1)

p = inter[0]
print("x,y = %.2f %.2f" % (p[0],p[1]))
p = inter[1]
print("x,y = %.2f %.2f" % (p[0],p[1]))