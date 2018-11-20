import sympy
print(sum(i for i in range(2,2000000) if sympy.isprime(i)))
