# Fibonacci, a first program in Python
import sys
#if (not sys.argv.isnumeric) or (sys.argv > 10000):
#    print('Limit not numeric or too big (select limit from 2 to 10000)')
#else:
limit = sys.argv
a,b = 0,1
while b < limit:
    print(b, end=',')
    a,b=b,a+b
