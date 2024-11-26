def a(n):
    return 4*2**n - 7*n

s = [a(n) for n in range(1,7)]
print("a_n gives:")
for t in s:
    print(t," ", end="")
print()

print()
print("recurrence gives:")
a = [1,2]
print("%d  %d  " % (a[0],a[1]), end="")

for n in range(3,7):
    v = 2*a[-1] - a[-2] + 2**n
    print("%d  " % v, end="")
    a.append(v)
print()

