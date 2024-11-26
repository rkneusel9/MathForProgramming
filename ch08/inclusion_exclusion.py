# integers in [1,200] divisible by 2, 5, and 7
A = {i for i in range(1,201) if (i%2) == 0}
B = {i for i in range(1,201) if (i%5) == 0}
C = {i for i in range(1,201) if (i%7) == 0}
print(len(A | B | C))

