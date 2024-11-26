# a_n = (2-sqrt(5))*phi**n + (2+sqrt(5))*(1-phi)**n
from decimal import *

getcontext().prec = 50
phi = (Decimal(1)+Decimal(5).sqrt()) / Decimal(2)
A = Decimal(1)
B = Decimal(1)

def L(n):
    return A*phi**n + B*(Decimal(1)-phi)**n

for n in range(1,100):
    f = str(L(n)).split(".")[0]
    print("L(%2d) = %s" % (n,f))

# 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ...

