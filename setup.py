# constructs and returns arbitrary function ----------------

import math
import numpy as np

def baseline(samples):
    return [0]*samples

def rising(start, stop, slope, samples):
    data = [0]*samples
    m = slope
    b = 0
    for i in range(start, stop):
        data[i] = m*(i-start) + b
    return data

def exponential(start, height, samples):
    data = [0]*samples
    tau = 300
    for i in range(start, samples):
        data[i] = height*math.exp(-(i-start)/tau)
    return data

def noise(samples):
    # add some noise to the signal
    return 2*np.random.randn(samples)

def signalConstruction():
    samples = 1000
    start = 300
    stop = 330
    slope = 5
    height = (stop-start)*slope
    base = baseline(samples)
    rise = rising(start, stop, slope, samples)
    expo = exponential(stop, height, samples)
    nois = noise(samples)
    data = [base[i] + rise[i] + expo[i] + nois[i] for i in range(samples)] 
    return data

# Trapezoidal filter ---------------------------------------

def trapFilter(data, tGap, tPeaking):
    dataFiltered = [0]*len(data)
    for k in range(2*tPeaking + tGap - 1, len(data)):
        dataFiltered[k] = (-sum(data[ (k-2*tPeaking-tGap+1):(k-tPeaking-tGap+1) ]) + sum(data[ (k-tPeaking+1):(k+1) ]))/tPeaking
    return dataFiltered