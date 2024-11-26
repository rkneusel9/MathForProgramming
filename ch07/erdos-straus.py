#
#  file:  erdos-straus.py
#
#  Brute force search for Erdos-Straus solutions for small n
#
#  4/n = 1/a + 1/b + 1/c, integer a,b,c positive integers,
#                         integer n>=2
#
#  Above true if:
#
#    4abc = n(bc+ac+ab)  (rewrite the equation)
#
################################################################

import pickle

solns = [[]]*9
limit = 250

for a in range(1,limit+1):
    for b in range(1,limit+1):
        for c in range(1,limit+1):
            lhs = 4*a*b*c
            rhs = (b*c+a*c+a*b)
            if (2*rhs == lhs):
                solns[0] = solns[0] + [(a,b,c)]
            if (3*rhs == lhs):
                solns[1] = solns[1] + [(a,b,c)]
            if (4*rhs == lhs):
                solns[2] = solns[2] + [(a,b,c)]
            if (5*rhs == lhs):
                solns[3] = solns[3] + [(a,b,c)]
            if (6*rhs == lhs):
                solns[4] = solns[4] + [(a,b,c)]
            if (7*rhs == lhs):
                solns[5] = solns[5] + [(a,b,c)]
            if (8*rhs == lhs):
                solns[6] = solns[6] + [(a,b,c)]
            if (9*rhs == lhs):
                solns[7] = solns[7] + [(a,b,c)]
            if (10*rhs == lhs):
                solns[8] = solns[8] + [(a,b,c)]

for i,s in enumerate(solns):
    print("%2d: % 3d solutions" % (i+2, len(s)))
print()

pickle.dump(solns, open("erdos-straus_solutions.pkl","wb"))

