""" funksjoner for IMAT1001"""

import cmath
import numpy as np
import sympy as sp

def show_polar(x, name=''):
    """
    viser komplekst tall på polar form
    """
    rho = abs(x)
    theta = np.degrees(cmath.phase(x))
    if len(name) < 1:
        print(f'{rho}<{theta}')

    else:
        print(f'{name}: {rho}<{theta}')

def linearize(f, a, x):
    """
    lineariser:
        f skal være en python funksjon
        a skal være lineariseringspunktet
        x skal være sympy symbol som skal brukes
    """
    df = sp.lambdify(x, sp.diff(f(x)))
    return f(a) + df(a)*(x - a)
