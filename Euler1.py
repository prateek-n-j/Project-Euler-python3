def sum_of_div_by_3_or_5(to):
    result = 0
    for i in range(1, to):
        if i % 3 ==0 or i % 5 ==0:
            result += i
    return result


print(sum_of_div_by_3_or_5(1000))
