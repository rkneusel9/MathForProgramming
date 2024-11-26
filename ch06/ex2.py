#  Compare complex a_n to the recurrence

def A(n):
    return complex(-3/8,-1/2)*complex(0,2)**n + complex(-3/8,1/2)*complex(0,-2)**n

s = [A(n) for n in range(1,7)]
print("a_n gives:")
for t in s:
    print(t," ", end="")
print()

print()
print("recurrence gives:")
a = [2,3]
print("%d  %d  " % (a[0],a[1]), end="")

for i in range(4):
    v = -4*a[-2]
    print("%d  " % v, end="")
    a.append(v)
print()

