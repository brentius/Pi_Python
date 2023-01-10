from decimal import *
 
D = Decimal
print("How many digits do you want to calculate to?")
digits =int(input())
print("Calculating", digits,"digits...")
a = n = D(1)
g, z, half = 1 / D(2).sqrt(), D(0.25), D(0.5)
for i in range(10):
    x = [(a + g) * half, (a * g).sqrt()]
    var = x[0] - a
    z -= var * var * n
    n += n
    a, g = x    
print(a * a / z)
print(digits,"digits calculated!")