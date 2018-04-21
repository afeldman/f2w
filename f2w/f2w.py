from scipy import constants as const

def w2f(wavelength, epsilon=0.00005):
    if wavelength < epsilon:
        return 0.0
    return float(float( const.c ) / float( wavelength ))

def f2w(frequence, epsilon=0.00005):
    if frequence < epsilon:
        return 0.0
    return float( float( const.c ) / float( frequence ))

