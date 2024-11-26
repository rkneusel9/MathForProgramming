# a_n = (1/sqrt(5))*(phi**n - (1-phi)**n)
from decimal import *

getcontext().prec = 50
phi = (Decimal(1)+Decimal(5).sqrt()) / Decimal(2)
C = Decimal(1) / Decimal(5).sqrt()

def F(n):
    return C*(phi**n - (Decimal(1)-phi)**n)

for n in range(1,100):
    f = str(F(n)).split(".")[0]
    print("F(%2d) = %s" % (n,f))

