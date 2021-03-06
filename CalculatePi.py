# Tiny script leaning heavily on functions from StackOverflow to calculate pi and output it to a file.

file = "" # Output file name here

def continued_fraction(a, b, base=10):
    """Generate digits of continued fraction a(0)+b(1)/(a(1)+b(2)/(...)."""
    (p0, q0), (p1, q1) = (a(0), 1), (a(1) * a(0) + b(1), a(1))
    k = 1
    while True:
        (d0, r0), (d1, r1) = divmod(p0, q0), divmod(p1, q1)
        if d0 == d1:
            yield d1
            p0, p1 = base * r0, base * r1
        else:
            k = k + 1
            x, y = a(k), b(k)
            (p0, q0), (p1, q1) = (p1, q1), (x * p1 + y * p0, x * q1 + y * q0)


digits = continued_fraction(lambda k: 0 if k == 0 else 2 * k - 1, lambda k: 4 if k == 1 else (k - 1)**2, 10)

with open(file, "w+") as f:
    while True:
        for k, digit in zip(range(5), digits):
            f.write(str(digit))
