#  CIs for dataset means
from stats import *

#  Petal width (cm) and length (cm) for I. setosa
width = [
0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1,
0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.4, 0.2, 0.5, 0.2, 0.2,
0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2,
0.2, 0.3, 0.3, 0.2, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2
]

length = [
1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5, 1.6, 1.4,
1.1, 1.2, 1.5, 1.3, 1.4, 1.7, 1.5, 1.7, 1.5, 1. , 1.7, 1.9, 1.6,
1.6, 1.5, 1.4, 1.6, 1.6, 1.5, 1.5, 1.4, 1.5, 1.2, 1.3, 1.4, 1.3,
1.5, 1.3, 1.3, 1.3, 1.6, 1.9, 1.4, 1.6, 1.4, 1.5, 1.4
]

#  Means and std dev
wm, ws = amean(width), std(width)
lm, ls = amean(length), std(length)

#  Critical values for 95th percentile CIs (alpha = 0.05)
z = 1.96
wt = t_critical(width,width, alpha=0.05, paired=True)
lt = t_critical(length,length, alpha=0.05, paired=True)

#  CIs
n = len(width)
wtlo, wthi = wm-wt*ws/sqrt(n), wm+wt*ws/sqrt(n)
wzlo, wzhi = wm-z*ws/sqrt(n), wm+z*ws/sqrt(n)
ltlo, lthi = lm-lt*ls/sqrt(n), lm+lt*ls/sqrt(n)
lzlo, lzhi = lm-z*ls/sqrt(n), lm+z*ls/sqrt(n)

print("Width: (alpha = 0.05)")
print("  t: [%0.5f, %0.3f, %0.5f]" % (wtlo,wm,wthi))
print("  z: [%0.5f, %0.3f, %0.5f]" % (wzlo,wm,wzhi))
print()
print("Length:")
print("  t: [%0.5f, %0.3f, %0.5f]" % (ltlo,lm,lthi))
print("  z: [%0.5f, %0.3f, %0.5f]" % (lzlo,lm,lzhi))
print()

#  Critical values for 99th percentile CIs (alpha = 0.01)
z = 2.5758
wt = t_critical(width,width, alpha=0.01, paired=True)
lt = t_critical(length,length, alpha=0.01, paired=True)

#  CIs
n = len(width)
wtlo, wthi = wm-wt*ws/sqrt(n), wm+wt*ws/sqrt(n)
wzlo, wzhi = wm-z*ws/sqrt(n), wm+z*ws/sqrt(n)
ltlo, lthi = lm-lt*ls/sqrt(n), lm+lt*ls/sqrt(n)
lzlo, lzhi = lm-z*ls/sqrt(n), lm+z*ls/sqrt(n)

print("Width: (alpha = 0.01)")
print("  t: [%0.5f, %0.3f, %0.5f]" % (wtlo,wm,wthi))
print("  z: [%0.5f, %0.3f, %0.5f]" % (wzlo,wm,wzhi))
print()
print("Length:")
print("  t: [%0.5f, %0.3f, %0.5f]" % (ltlo,lm,lthi))
print("  z: [%0.5f, %0.3f, %0.5f]" % (lzlo,lm,lzhi))
print()

