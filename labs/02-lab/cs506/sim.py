from cmath import nan
import math
from multiprocessing.sharedctypes import Value

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")

    if x == y:
        return 0

    res = 0
    
    # intersect
    # Intersect
    seen = {}
    count_intersect = 0
    for elem in x:
        if elem not in seen:
            if elem in y:
                count_intersect += 1
                seen[elem] = 1
    

    count_union = len(x) + len(y) - 2 * count_intersect
    if count_union == 0:
        return 0

    res = (count_union - count_intersect) / count_union
    return res

def cosine_sim(x, y):
    res = 0
    
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")

    numerator = 0
    # Dot product of x and y
    for i in range(len(x)):
        x_i = x[i]
        y_i = y[i]

        numerator += x_i * y_i

    # norm
    norm_x = norm(x)
    norm_y = norm(y)

    if norm_x == 0:
        return 0
    
    if norm_y == 0:
        return 0

    res = numerator / (norm_x * norm_y)

    return res

def norm(x):
    res = 0

    numerator = 0
    for elem in x:
        numerator += (elem * elem)
    
    res = math.sqrt(numerator)
    return res

# Feel free to add more
