# div and mod functions implementing Euclidean division
# RTK, 18-Jan-2023 (Happy 87th TC!)

def divmod(a,b):
    """calculate the integer quotient and remainder"""
    if ((a>0) and (b>0)) or ((a<0) and (b>0)):
        return a//b, a%b
    elif (a>0) and (b<0):
        return -(a//abs(b)), a%abs(b)
    else:
        return abs(a//abs(b)), a%abs(b) 

def div(a,b):
    """Euclidean integer division"""
    return divmod(a,b)[0]

def mod(a,b):
    """Euclidean integer modulo"""
    return divmod(a,b)[1]

