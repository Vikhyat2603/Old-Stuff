import numpy as n    ,   matplotlib.pyplot as p

global h,w
h=1
w=1

def function(x):
          return (n.sin(x**2))

X = n.linspace(-10, 10, 1000, endpoint=False)
F = function(X)
p.plot(X,F)
p.show()
