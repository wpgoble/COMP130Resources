import numpy as np
from matplotlib import pyplot as plt

index, sqrt = np.loadtxt("points.csv",
                         usecols = (0, 3),
                         delimiter = ",",
                         skiprows=1,
                         unpack=True)

print(index)
print("-"*45)
print(sqrt)

plt.plot(index, sqrt, marker="D")
plt.show()
