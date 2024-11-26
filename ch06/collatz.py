import sys

def collatz(a, n=1000):
    """Return the sequence for a up to n terms"""

    seq = [a]
    while (a != 1) and (len(seq) < n):
        if ((a%2) == 0):
            a = a//2
        else:
            a = 3*a+1
        seq.append(a)
    return seq


if (__name__ == "__main__"):
    if (len(sys.argv) == 1):
        print()
        print("collatz <n>")
        print()
        print("  <n> -- a positive integer")
        print()
        exit(0)

    print(collatz(int(sys.argv[1])))

