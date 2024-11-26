# SOP, POS, and complements

def g(a,b,c):
    return (a or b and not c) and (a and b or not b and c)

def SOP(a,b,c):
    return a and not b and c  or  a and b and not c  or  a and b and c

def POS(a,b,c):
    return (a or b or c) and (a or b or not c) and (a or not b or c) and (a or not b or not c) and (not a or b or c)

def gc(a,b,c):
    return not a and not b and not c  or  not a and not b and c  or  not a and b and not c  or  not a and b and c  or  a and not b and not c

def gc2(a,b,c):
    return (not a or b or not c) and (not a or not b or c) and (not a or not b or not c)

def simp(a,b,c):
    return a and (not b and c or b)

def k(a,b,c):
    return a and b or a and c  #a and (b or c)

print("a b c g S P C 2 s k")
print("-------------------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d %d %d %d %d %d %d" % (a,b,c, g(a,b,c), SOP(a,b,c), POS(a,b,c), gc(a,b,c), gc2(a,b,c), simp(a,b,c), k(a,b,c)))

