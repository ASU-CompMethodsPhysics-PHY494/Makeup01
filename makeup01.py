# Skeleton code for ASU PHY494 Makeup01
#
# Copyright (c) 2016-2021 Oliver Beckstein
# All rights reserved.
#


import numpy as np
import scipy.integrate

# def initial_values_qmhosc(n):
#     """Return physically correct initial values at x=0 for QM SHOSC.
#
#     Convention: always choose the positive values for psi(0) and psi'(0).
#
#     Arguments
#     ---------
#     n : int
#         energy level (0, 1, 2, ...)
#
#     Returns
#     -------
#     y :  array
#         initial values [psi(0), psi'(0)]
#     """



def f_qmhosc(t, y, E):
    """Standard form derivative vector dy/dt = f

    Equation to be solved:

       -1/2 u'' + 1/2 x^2 u = E u

    """
    # replace the next line with your code
    raise NotImplementedError

def ode_qmhosc(x, y0_0, y1_0, n=0):
    """Solve -1/2 u'' + 1/2 x^2 u = E u.

    Initial conditions (at x0 = x[0]):

      y0_0: value u(x0)
      y1_0: derivative du/dx at x0
    """
    # replace the next line with your code
    raise NotImplementedError

    # HINT: You can wrap the f_qmhosc function as f() so that
    #       f() has exactly the signature required by
    #       scipy.integrate.solve_ivp():
    #
    # def f(t, y):
    #      return f_qmhosc(t, y, E)
    #
    #
    # Then use *this* f as input for the solver.


    return y




