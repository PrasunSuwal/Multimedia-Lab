import numpy as np

def dct1d(signal):
    N = len(signal)
    dct_result = np.zeros(N)
    
    for k in range(N):
        sum_val = 0.0
        for n in range(N):
            sum_val += signal[n] * np.cos(np.pi * k * (2*n + 1) / (2 * N))
        dct_result[k] = sum_val
    
    return dct_result

# Example usage:
signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
dct_result = dct1d(signal)
print("Original Signal:", signal)
print("DCT Result:", dct_result)
