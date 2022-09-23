from scipy.spatial import distance
import numpy.linalg as linear

x = [0]
y = [0, 0]

print(linear.norm(x))
print(linear.norm(y))
print(distance.cosine(x, y))