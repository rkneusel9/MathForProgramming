# Recursive Fibonacci sequence generator
import time
import matplotlib.pylab as plt

# iterative, no recursion
def fib0(n):
    a,b = 0,1
    while (n > 0):
        a,b = b,a+b
        n -= 1
    return a

# push down single recursive call
def fib1(n):
    def f(a,b,n):
        if (n == 0):
            return a
        else:
            return f(b,a+b,n-1)
    return f(0,1,n)

# horrible push up double recursive call
def fib(n):
    if (n < 3):
        return 1
    else:
        return fib(n-1) + fib(n-2)


if (__name__ == "__main__"):
    N = [2,5,10,15,20,25,30,35,40]
    t = []

    for n in N:
        s = time.time()
        _ = fib(n)
        t.append(time.time()-s)

    plt.plot(N,t, marker='o', fillstyle='none', color='k')
    plt.xlabel("$F_n$")
    plt.ylabel("Time (s)")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("fibonacci_recursive.png", dpi=300)
    plt.savefig("fibonacci_recursive.eps", dpi=300)
    plt.close()

