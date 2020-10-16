import numpy as np
import pint
from scipy import constants as const

ureg = pint.UnitRegistry()

def funit(x):
    return {
        "GHz": 1E9 / ureg.s,
        "MHz": 1E6 / ureg.s,
        "KHz": 1E3 / ureg.s,
        "Hz": ureg.Hz
    }[x]

def wunit(x):
    return {
        "m": ureg.meter,
        "dm": ureg.dm,
        "cm": ureg.cm,
        "mm": ureg.mm
    }[x]

def w2f(wavelength, unit="m", epsilon=np.finfo(float).eps):
    if wavelength < epsilon:
        return np.float(0.0)

    l = np.float(wavelength)*wunit(unit)
    c = np.float(const.speed_of_light)*(ureg.m/ureg.s)

    return c / l


def f2w(frequence, unit="GHz", epsilon=np.finfo(float).eps):
    if frequence < epsilon:
        return np.float(0.0)

    f = np.float(frequence)*funit(unit)
    c = np.float(const.speed_of_light)*(ureg.m/ureg.s)

    return c / f
