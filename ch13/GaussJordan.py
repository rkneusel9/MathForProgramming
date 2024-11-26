#
#  file:  GaussJordan.py
#
#  Implements Gauss-Jordan elimination of a matrix represented
#  as a list of lists.
#
#  By Jarno Elonen (elonen@iki.fi), April 2005, public domain
#  (https://elonen.iki.fi/code/misc-notes/python-gaussj/index.html)
#
################################################################

def GaussJordan(m, eps = 1e-10):
    """Put matrix into reduced row-echelon form.  In-place calculation.
       Returns True if successful, False if m is singular"""

    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
        maxrow = y
        for y2 in range(y+1, h):    # Find max pivot
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for y2 in range(y+1, h):    # Eliminate column y
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # Backsubstitute
        c  = m[y][y]
        for y2 in range(0,y):
            for x in range(w-1, y-1, -1):
                m[y2][x] -=  m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w):       # Normalize row y
            m[y][x] /= c
    return True

