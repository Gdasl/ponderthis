import itertools

def farey(n):
    return  (n*(n+3))//2 - sum(farey(n//k) for k in range(2, n+1))


dp = dict() # sometimes, dp stands for dynamic programming

def farey2(n):
    if dp.get(n):
        return dp.get(n)
    else:
        dp[n] = (n * (n + 3)) // 2 - sum(farey2(n // k) for k in xrange(2, n + 1))
    return dp[n]

#print farey(10000)

#min is 57356
#max is 181379




def guessables(num):
    guesses = []
    for p in itertools.permutations(xrange(10),num):
        if p[0] != 0:
            guesses.append(''.join(map(str, p))) 
    return guesses

a = guessables(10)
def go():
    dic2 = dict()

    for i in xrange(57356, 181379):
        if str(farey2(i)) in a:
            print i
        

#go()
