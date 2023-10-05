import numpy as np
import matplotlib.pyplot as plt


num_walkers = 100
num_steps = 1000
steps = np.random.choice([-1, +1], size=[num_walkers, num_steps])
distance = np.cumsum(steps, axis=1)

plt.plot(distance.T)
plt.show()
