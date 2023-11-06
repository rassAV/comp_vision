import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

def filling_factor(region):
    return region.image.mean()

def recognize(region):
    if filling_factor(region) == 1: # -
        return '-'
    else:
        match region.euler_number:
            case -1: # B 8
                if 1 in region.image.mean(0):
                    return 'B'
                return '8'
            case 0: # A 0 P D
                if 1 in region.image.mean(0):
                    if region.image[-1][:region.image.shape[1]//2].mean() == 1:
                        return 'D'
                    return 'P'
                tmp = region.image.copy()
                tmp[-1, :] = 1
                tmp_labeled = label(tmp)
                tmp_regions = regionprops(tmp_labeled)
                if tmp_regions[0].euler_number == -1:
                    return 'A'
                return '0'
            case 1: # 1 W X * /
                if 1 in region.image.mean(0):
                    return "1"
                tmp = region.image.copy()
                tmp[[0, -1], :] = 1
                tmp_labeled = label(tmp)
                tmp_regions = regionprops(tmp_labeled)
                euler = tmp_regions[0].euler_number
                if euler == -1:
                    return 'X'
                elif euler == -2:
                    return 'W'
                if region.eccentricity > 0.5:
                    return '/'
                else:
                  return '*'
    return 'unknown'

img = plt.imread('symbols.png')

binary = img.mean(2)
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

counts={}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1

print(counts)
print(1 - counts.get('unknown', 0) / labeled.max())
