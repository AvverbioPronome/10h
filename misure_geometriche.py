import numpy as np
def sfera(r):
    return {
        "cerchio_massimo": 2 * np.pi * r,
        "superficie": 4 * np.pi * r**2,
        "volume": 4/3 * np.pi * r**3}