num = []
for i in range(1,21):
    num.append(i)


def divi_by_num(a):
    for i in range(0,len(num)):
        if a % num[i] != 0:
            return 0
    else:
        return 1

multiple = 1
for i in range(9699690, 9699690**2, 5):
    if divi_by_num(i) == 1:
        multiple = i
        break
print(multiple)