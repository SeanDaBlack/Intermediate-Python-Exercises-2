import numpy as np
from numpy.random import default_rng

if __name__ == "__main__":

    l = default_rng().random(10)
    print(l)

    print(
        f"Mean: {l.mean()}, Median: {np.median(l)}, Standard Deviation: {l.std()}")
