from decimal import *
import time
D = Decimal
print("How many digits do you want to calculate to?")
getcontext().prec = digits=int(input())
print("Calculating",digits,"digits...")
start=time.time()
a = n = D(1)
g, z, half = 1 / D(2).sqrt(), D(0.25), D(0.5)
for i in range(10):
    x = [(a + g) * half, (a * g).sqrt()]
    var = x[0] - a
    z -= var * var * n
    n += n
    a, g = x
print(a * a / z)
end=time.time()
print(digits,"digits calculated!")
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Time taken:","{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))