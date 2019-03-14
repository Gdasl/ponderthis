# January

from operator import mul
from math import *
from primefac import primefac

def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = []
    for i in xrange(n/2):
        sieve.append(True)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]



def farey(n):
    return  (n*(n+3))//2 - sum(farey(n//k) for k in range(2, n+1))


dp = dict() # sometimes, dp stands for dynamic programming

def farey2(n):
    print n
    if dp.get(n):
        return dp.get(n)
    elif dp.get(n-1):
        dp[n] = (dp.get(n-1)+eulerphi(n))
        print n, dp[n]
        return dp.get(n)
    else:
        dp[n] = (n * (n + 3)) // 2 - sum(farey2(n // k) for k in xrange(2, n + 1))
    return dp[n]

#print farey(10000)

#min is 57356
#max is 181379


import itertools

def guessables(num):
    guesses = []
    for p in itertools.permutations(xrange(10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p))) 
    return guesses

def guessables_hex(maxlen = 1000):
    for p in itertools.permutations('0123456789abcdef',16):
        if p[0] != '0':
            guesses.append(int(''.join(map(str, p)),16)) 
    return guesses

#a = guessables(10)
def go():
    dic2 = dict()

    for i in xrange(57356, 181379):
        if str(farey2(i)) in a:
            print i

        
##guesses = []
##for p in itertools.permutations('123456789abcdef0',16):
##        if p[0] != '0':
##            guesses.append(int(''.join(map(str, p)),16)) 
##    

#farey2(1000000002)

def primeFactorsD(n):
    max_p = rwh_primes1(n+1)
    arr = []
    for i in max_p:
        while not n%i:
            n = n/i
            arr.append(i)
    return arr


def eulerphi(n):
    totient = n
    for factor in primefac(n):
        totient -= totient // factor
    return totient
