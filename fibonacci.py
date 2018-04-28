# Fibonacci, a first program in Python
limit = 5000
a,b = 0,1
while b < limit:
    print(b, end=',')
    a,b=b,a+b
