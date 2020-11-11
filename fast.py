"""
Representation of efficiency
    ^
 %  | ...............
rec.|                ····..
    |                      ·
    |                       :
    |                        :
    +------------------------------>
                            Cut Probability Value

Data is taken from all_bins_NTRACKS_tracks.txt, which is written by
kalmanTRAG.py with flags:
  - rd_seed: int or None = None
  - single_run: bool = False
  - do_efficiency: bool = True
  - if_repr: bool = False
  - if_final_prints: bool = False
  - if_save_diff: bool = False
  - NTRACKS = int (quantity of desired generated tracks)

@author: Miguel Cruces
"""

import numpy as np
import matplotlib.pyplot as plt

ntracks = 1
filename = f"all_bins_{ntracks}_tracks.txt"
a = np.loadtxt(filename)

rate = []
for line in a.T:
    rate.append(line[ntracks] / np.sum(line))

rate = np.asarray(rate)
x_rate = np.arange(len(rate))

plt.figure(filename)
plt.plot(x_rate / 100, rate * 100)
plt.ylabel("Reconstructed SAETAs %")
plt.grid(axis="both")
plt.xlabel("Cut Value")
plt.savefig(f"{filename[:-4]}.png")
