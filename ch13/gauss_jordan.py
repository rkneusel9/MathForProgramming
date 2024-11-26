def gauss_jordan(m, eps = 1.0/(10**10)):
  """Puts given matrix (2D array) into the Reduced Row Echelon Form.
     Returns True if successful, False if 'm' is singular.
     NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
     Written by Jarno Elonen in April 2005, released into Public Domain"""
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

