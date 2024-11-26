# Karnaugh with z(a,b,c,d)

def z(a,b,c,d):
    return a and not b and not c and not d  or  not a and not b and c and not d  or  a and b and not c  or  not a and not c and d  or  a and c

def m(a,b,c,d):
    return b and not c and not d  or  not a and not c and d  or  not a and b and d  or  a and not b and d  or  a and b and c and not d

print("a b c d z m")
print("-----------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            for d in [0,1]:
                print("%d %d %d %d %d %d" % (a,b,c,d, z(a,b,c,d), m(a,b,c,d)))

