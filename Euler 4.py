import math


def is_palindrome(num):
    s = str(num)
    x = math.ceil((len(s)/2))
    s1 = s[0: x]
    s2 = s[x:]
    return s1 == s2[::-1]


res = []
for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        if is_palindrome(z):
            res.append(z)
result = max(res)


print(result)
