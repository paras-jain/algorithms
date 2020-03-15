def karatsuba(x, y):
    if x < 10 and y < 10:
        return x*y
    
    m = max(len(str(x)),len(str(y)))
    n = m // 2
    
    a = x // (10**n)
    b = x % (10**n)
    c = y // (10**n)
    d = y % (10**n)
    
    p = karatsuba(a, c)
    q = karatsuba(b, d)
    r = karatsuba(a+b, c+d) - p - q
    
    return p*(10**(n*2)) + r*(10**n) + q

s = int(input("Enter first number: "))
t = int(input("Enter second number: "))
print(karatsuba(s, t))
