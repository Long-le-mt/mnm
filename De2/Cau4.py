uscln = lambda a, b: a if (b == 0) else uscln(b, a % b)

print(uscln(15, 20))