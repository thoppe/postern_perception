import numpy as np
import pylab as plt
import seaborn as sns

angles = np.load("angles.npy")
xr = np.load("xr.npy")

print(xr[:, 0, 0, 0])
print(xr.shape)

# print(angles)
# sns.distplot(angles[:,1])
# plt.show()
