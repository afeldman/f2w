import numpy as np
import pint
from scipy import constants as const

ureg = pint.UnitRegistry()

def funit(x):
    _units = {
        "ghz": 1E9 / ureg.s,
        "mhz": 1E6 / ureg.s,
        "khz": 1E3 / ureg.s,
        "hz": ureg.Hz
    }

    if x in _units.keys():
        return _units[x]
    else:
        print(f"unit {x} not found")
        return ureg.Hz


def wunit(x):

    _units = {
        "m": ureg.meter,
        "dm": ureg.dm,
        "cm": ureg.cm,
        "mm": ureg.mm
    }

    if x in _units.keys():
        return _units[x]
    else:
        print(f"unit {x} not found")
        return ureg.meter

def w2f(wavelength, unit=None, epsilon=np.finfo(float).eps):
    if wavelength < epsilon:
        return np.float(0.0)

    _unit = 0
    if unit is not None:
        _unit = wunit(unit)
        c = np.float(const.speed_of_light)*(ureg.m/ureg.s)
    else:
        _unit = 1.0
        c = np.float(const.speed_of_light)

    l = np.float(wavelength)*_unit

    return c / l


def f2w(frequence, unit=None, epsilon=np.finfo(float).eps):
    if frequence < epsilon:
        return np.float(0.0)

    _unit = 0
    if unit is not None:
        _unit = wunit(unit)
        c = np.float(const.speed_of_light)*(ureg.m/ureg.s)
    else:
        _unit = 1.0
        c = np.float(const.speed_of_light)

    f = np.float(frequence)*_unit

    return c / f
