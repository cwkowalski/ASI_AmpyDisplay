import numpy as np
from math import sqrt

class cubic_interp1d():
    def __init__(self, x, y):
        self.x = np.asfarray(x)
        self.y = np.asfarray(y)

    def interp1d(self, x0):
        """
       Interpolate a 1-D function using cubic splines.
         x0 : a float or an 1d-array
         x : (N,) array_like
             A 1-D array of real/complex values.
         y : (N,) array_like
             A 1-D array of real values. The length of y along the
             interpolation axis must be equal to the length of x.

       Implement a trick to generate at first step the cholesky matrice L of
       the tridiagonal matrice A (thus L is a bidiagonal matrice that
       can be solved in two distinct loops).

       additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf
       """
        if np.any(np.diff(self.x) < 0):
            indexes = np.argsort(self.x)
            self.x = self.x[indexes]
            self.y = self.y[indexes]

        size = len(self.x)

        xdiff = np.diff(self.x)
        ydiff = np.diff(self.y)

        # allocate buffer matrices
        Li = np.empty(size)
        Li_1 = np.empty(size-1)
        z = np.empty(size)

        # fill diagonals Li and Li-1 and solve [L][y] = [B]
        Li[0] = sqrt(2*xdiff[0])
        Li_1[0] = 0.0
        B0 = 0.0 # natural boundary
        z[0] = B0 / Li[0]

        for i in range(1, size-1, 1):
            Li_1[i] = xdiff[i-1] / Li[i-1]
            Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
            Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
            z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

        i = size - 1
        Li_1[i-1] = xdiff[-1] / Li[i-1]
        Li[i] = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
        Bi = 0.0 # natural boundary
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

        # solve [L.T][x] = [y]
        i = size-1
        z[i] = z[i] / Li[i]
        for i in range(size-2, -1, -1):
            z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

        # find index
        index = self.x.searchsorted(x0)
        np.clip(index, 1, size-1)

        xi1, xi0 = self.x[index], self.x[index-1]
        yi1, yi0 = self.y[index], self.y[index-1]
        zi1, zi0 = z[index], z[index-1]
        hi1 = xi1 - xi0

        # calculate cubic
        f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
             zi1/(6*hi1)*(x0-xi0)**3 + \
             (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
             (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
        return f0
