def PhysicalRandom(f):
	return ord(f.read(1)) % 10
f = open("/dev/urandom","rb")
print("0.", end="")
while True: print("%d" % PhysicalRandom(f), end="")

