






def power(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x,n//2) * power(x,n//2)
    else:
        return x*power(x,n//2) * power(x,n//2)


power(2,7)