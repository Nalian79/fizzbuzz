# Creating the FizzBuzz app from scratch.

# For FizzBuzz v1, we are going to print all the numbers
# from 1 to 100. For every number divisible by 3, we will print 
# fizz instead of the number.  For every number divisible by 5,
# we will print buzz.  If the number is divisible by both, we
# will print fizzbuzz.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print 'fizzbuzz'
    elif i % 3 == 0:
        print 'fizz'
    elif i % 5 == 0:
        print 'buzz'
    else:
        print i
