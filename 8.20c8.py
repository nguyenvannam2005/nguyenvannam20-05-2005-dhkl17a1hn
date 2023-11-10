import math

def approximate_exp(x):
    n = 1
    approximation = 1 + x**2 / n
    
    while abs(math.exp(x) - approximation) > 1e-4:
        n += 1
        approximation = 1 + x**2 / n
    
    return approximation

x = 1
approximation = approximate_exp(x)
print(f"e ≈ {approximation:.5f}")