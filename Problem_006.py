
sum_of_squares = 0
square_of_sums = 0
for i in range(0, 101):
    sum_of_squares += pow(i, 2)
    square_of_sums += i
square_of_sums = pow(square_of_sums, 2)
print(square_of_sums - sum_of_squares)