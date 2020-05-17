#Question 1:

# Accept two integer numbers from a user and return their product and
# if the product is greater than 1000, then return their sum

num1 = int(input('Enter the first number : '))
num2 = int(input('Enter Second number : '))

product = num1 * num2

if product > 1000:
    print(num1 + num2)
else:
    print('The output is : {} '.format(product))
