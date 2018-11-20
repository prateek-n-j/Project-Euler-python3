num_list = []
for i in range(1,101):
    num_list.append(i)
sum_of_squares = 0
for i in range(1,101):
    sum_of_squares += i**2
print(sum_of_squares)
square_of_sum = sum(num_list)**2
print(square_of_sum)
print(square_of_sum-sum_of_squares)
