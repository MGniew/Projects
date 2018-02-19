'''calculates pi to n didgit'''
from decimal import Decimal, getcontext


def fraction_generator_maclaurin(n):
    '''Calculates fractions for macuarin series'''
    x = 1
    y = 1
    for i in range(n):
        yield Decimal(y * Decimal(4)/Decimal(x))
        x += 2
        y *= -1


def calculate_pi_maclaurin():
    '''Calculates pi using Maclaurin series (pi = 4/3 - 4/5 + 4/7...'''
    sum = Decimal(0)
    for i in fraction_generator_maclaurin(50000):
        sum += i
    return sum


def calculate_pi_bbp_series(n):
    '''Simple bbp alg. '''
    k = 0
    for i in range(n):
        a = 120 * k**2 + 151 * k + 47
        b = 512 * k**4 + 1024 * k**3 + 712 * k**2 + 194 * k + 15
        yield Decimal(1)/Decimal(16**k) * Decimal(a)/Decimal(b)
        k += 1


def bbp_sum(j,n):
    '''Bbp digit-extraction algorithm'''
    
    #left
    sl = 0.0
    k = 0
    while k <= n:
        r = 8*k+j
        sl = (sl + pow(16, n-k, r) / r) % 1.0
        k += 1

    #right
    sr = 0.0
    while 1:
        srn = sr + pow(16, n-k) / (8*k+j)
        if sr == srn:
            break
        else:
            sr = srn
        k += 1
    return sl + sr


def calculate_pi_bbp(n):
    n -= 1
    x = (4*bbp_sum(1, n) - 2*bbp_sum(4, n) - bbp_sum(5, n) - bbp_sum(6, n)) % 1.0
    return "%1x" % int(x * 16)     


if __name__ == '__main__':

    x = int(input("Enter a precision: "))
    getcontext().prec = x
    print("maclaurin:")
    print(calculate_pi_maclaurin())

    print("bbp series (bbp series):")
    a = Decimal(0)
    for dig in calculate_pi_bbp_series(x):
        a += dig
    print(a)

    print("bbp (digit by digit in hex):")
    print(3, end='.')
    for i in range(x - 1):
    	print(calculate_pi_bbp(i),end='')
    print()

