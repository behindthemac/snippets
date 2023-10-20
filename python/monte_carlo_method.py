import numpy as np
from scipy.spatial import distance


origin = np.zeros(2)
n = 10 ** 6
points = np.random.rand(n, 2)

d = np.array([distance.euclidean(origin, point) for point in points])
count = np.count_nonzero(d < 1)

pi = count / n * 4
print(pi)
