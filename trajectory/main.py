import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

figures = [[], [], []]
for i in range(100):
  image = label(np.load(f"h_{i}.npy"))
  regions = sorted(regionprops(image), key = lambda x: x.area)
  for j in range(3):
    figures[j].append(regions[j].centroid)
figures = np.array(figures)

plt.plot(figures[0, :, 0], figures[0, :, 1])
plt.plot(figures[1, :, 0], figures[1, :, 1])
plt.plot(figures[2, :, 0], figures[2, :, 1])
plt.show()
