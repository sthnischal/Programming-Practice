# Question 2:

# Given a range of first 10 numbers, Iterate from start number to the end number and
# print the sum of the current number and previous number

# range function for generating number
num = range(1,11)

print('Printing current and previous number sum in a given range(10)')
# iterate numbers
for i in num:
    sum = i + (i-1)
    print('Current Number {} Previous Number  {}  Sum:  {}'.format(i, i-1, sum))
    # print('The Current numner is : {}'.format(i))


# print(num[0])