a = 1

while a <= 9:
    b = 1
    while b <= a:
        print(a, " * ", b, "=", a * b, end="|")
        b += 1
    print("")
    a += 1
