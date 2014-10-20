# Creating the FizzBuzz app from scratch.

# FizzBuzz v2, time to prompt for inputs!  Either run this 
# script with a minimum and maximum number - not inclusive. If
# the user does not supply arguments, they will be prompted
# for two numbers.
#
# FizzBuzz game:
# For every number divisible by 3, we will print 
# fizz instead of the number.  For every number divisible by 5,
# we will print buzz.  If the number is divisible by both, we
# will print fizzbuzz.

import sys

if len(sys.argv) == 1:
    min_num = int(raw_input("Please enter min number: "))
    max_num = int(raw_input("Please enter a max number: "))
else:
    min_num = int(sys.argv[1])
    max_num = int(sys.argv[2])


for num in range(min_num, max_num):
    if num % 3 == 0 and num % 5 == 0:
        print 'fizzbuzz'
    elif num % 3 == 0:
        print 'fizz'
    elif num % 5 == 0:
        print 'buzz'
    else:
        print num
