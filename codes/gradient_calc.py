import numpy as np


def gradient_calculation(x, y):

    print("AHOJS")
    gradient = np.array([])
    len = np.size(y)

    for i in range(0, len):
        if i > 0 and i < len-1:
            gradient = np.append(
                gradient, (y[i + 1] - y[i - 1])/(x[i + 1] - x[i - 1]))
        # avoiding out of bounds
        elif i == 0:  # first element
            gradient = np.append(gradient, (y[1] - y[0]) /
                                 ((x[1] - x[0])))
        else:  # last element
            gradient = np.append(gradient, (y[len - 1] - y[len - 2]) /
                                 ((x[len - 1] - x[len - 2])))

    return gradient
