# exercises

def IsTheSame2(F,G):
    """Do the expressions generate the same truth table?"""

    def Apply(a,b,E):
        """Apply a and b to an expression, E"""
        return eval(E)

    A = []
    B = []
    for a in [0,1]:
        for b in [0,1]:
            A.append(Apply(a,b,F))
            B.append(Apply(a,b,G))
    return A == B

def IsTheSame3(F,G):
    def Apply(a,b,c,E):
        return eval(E)
    A = []
    B = []
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                A.append(Apply(a,b,c,F))
                B.append(Apply(a,b,c,G))
    return A == B

#
#  main
#
print(IsTheSame3("not (a and b and c)", "not a or not b or not c"))
print(IsTheSame2("not a or not b or a and b", "1"))
print(IsTheSame2("not a and (not a or not b)", "not a"))
print(IsTheSame3("a and not c or not a and b or not (a and c)", "not (a and c)"))
print(IsTheSame2("not (a or (a and b or not b))", "not a and b"))
print()
print(IsTheSame3("(a and b) or (a and c)", "(b or c) and a"))

