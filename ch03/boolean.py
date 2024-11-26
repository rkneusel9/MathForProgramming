# Example Boolean functions

def f(x,y):
    return not x and (x or not y)

print("x y f")
print("-----")
for x in [0,1]:
    for y in [0,1]:
        print("%d %d %d" % (x,y,f(x,y)))
print()

def fc(x,y):
    return x or not x and y

print("x y fc")
print("------")
for x in [0,1]:
    for y in [0,1]:
        print("%d %d %d" % (x,y,fc(x,y)))
print()

def g(a,b,c):
    return (a or b and not c) and (a and b or not b and c)

print("a b c g")
print("-------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,g(a,b,c)))
print()

def gc(a,b,c):
    return not a and (not b or c) or (not a or not b) and (b or not c)

print("a b c gc")
print("--------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,gc(a,b,c)))
print()

def gd(a,b,c):
    return (a and (b or not c)) or ((a or b) and (not b or c))

print("a b c gd")
print("--------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,gd(a,b,c)))
print()

def e(a,b,c):
    return (a and not b and c) or (not a and b and not c) or (a and b and c)

print("a b c e")
print("-------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,e(a,b,c)))
print()

def ed(a,b,c):
    return (a or not b or c) and (not a or b or not c) and (a or b or c)

print("a b c ed")
print("--------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,ed(a,b,c)))
print()

def ec(a,b,c):
    return (not a or b or not c) and (a or not b or c) and (not a or not b or not c)

print("a b c ec")
print("--------")
for a in [0,1]:
    for b in [0,1]:
        for c in [0,1]:
            print("%d %d %d %d" % (a,b,c,ec(a,b,c)))

