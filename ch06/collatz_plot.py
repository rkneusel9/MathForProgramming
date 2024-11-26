from collatz import *
import numpy as np
import matplotlib.pylab as plt

#  Figure 11.11 in Pickover, "Computers, Pattern, Chaos and Beauty" (1990)
x = []
y = []
for n in range(1,1001):
    s = collatz(n)
    for t in s:
        if (t <= 1000):
            x.append(n)
            y.append(t)

plt.plot(x,y, marker='o', markersize=0.3, color='k', linestyle='none')
plt.xlabel("$n$")
plt.ylabel("Sequence")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("collatz_sequence_plot.png", dpi=300)
plt.savefig("collatz_sequence_plot.eps", dpi=300)
plt.close()

#  Bar plot of maximum sequence values
s = []
for n in range(5,201):
    s.append(max(collatz(n)))
plt.bar(range(5,201), s, width=0.6, color='k')
plt.xlabel("$n$")
plt.ylabel("Maximum sequence value")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("collatz_max_plot.png", dpi=300)
plt.savefig("collatz_max_plot.eps", dpi=300)
plt.close()

#  Bar plot of sequence lengths
s = []
for n in range(5,201):
    s.append(len(collatz(n)))
plt.bar(range(5,201), s, width=0.6, color='k')
plt.xlabel("$n$")
plt.ylabel("Sequence length")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("collatz_length_plot.png", dpi=300)
plt.savefig("collatz_length_plot.eps", dpi=300)
plt.close()

