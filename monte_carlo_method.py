import numpy as np
from scipy.spatial import distance


n = 10 ** 4
o = np.zeros(2)
c = np.random.rand(n, 2)
d = np.array([distance.euclidean(o, c[i]) for i in range(n)])
x = np.count_nonzero(d < 1)
pi = 4.0 * x / n
print(pi)
