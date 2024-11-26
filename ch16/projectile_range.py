#  Search for the angle leading to maximum range
import numpy as np
import sys
import os

if (len(sys.argv) == 1):
    print()
    print("projectile_range <muzzle> <k>")
    print()
    print("  <muzzle> - muzzle velocity (m/s)")
    print("  <k>      - drag coefficient")
    print()
    exit(0)

muzzle = float(sys.argv[1])
k = float(sys.argv[2])

mag, rnge = 0, -1
for angle in np.linspace(1,50,99):
    cmd = "python3 projectile.py " + str(angle) + " " + str(muzzle) + " " + str(k) + " 0.001 no >/tmp/ttt"
    os.system(cmd)
    t = open("/tmp/ttt").read()[:-1]
    r = float(t.split()[-2])
    if (r > rnge):
        rnge = r
        mag = angle

print("Maximum range of %0.2f meters at %0.1f degrees" % (rnge, mag))


