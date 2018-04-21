#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--f', default='0.0' ,help='frequence in [Hz]', type=float)
parser.add_argument('--l', default='0.0', help='wave length in [m]', type=float)

result = parser.parse_args()

c = 2.99792458E8 #speed of light
t = 0.0#time of periode
epsilon = 1E-4

l = float(result.l)
f = float(result.f)

if l > epsilon:
    f=c/l
    print("The frequence:\t"+str(f)+" [Hz]")
    print("Time of periode:\t"+str(1/f)+" [s]")
    f=0.0

if f > epsilon:
    l=c/f
    print("The wave length:\t"+str(l)+" [m]")
    l=0.0