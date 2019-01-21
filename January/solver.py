import itertools
#primes = [int(i) for i in open('gistfile1.txt','r').read().split(',')]
#squares = [i**2 for i in primes]

maxi =  40
real_squares = [i**2 for i in range(1,maxi)]
def sumis(n):
    if n%2:
        n_ = n+1
    else:
        n_ = n
    return [(i,n-i) for i in range(1,n_/2)]
        

tuplis = [sumis(i) for i in real_squares]


def check_2(a,b):
    arr = []
    for i in range(1,(maxi-1)**2):
        if i+a in real_squares and i+b in real_squares:
            arr.append(i)
    return arr


def ulticheck(tu):
    arri = [check_2(i[0],i[1]) for i in itertools.combinations(tu,2)]
    result = set(arri[0])
    for s in arri[1:]:
        result.intersection_update(s)
    return result

def go(siz):
    print 'Max: %d'%maxi
    tested = []
    a=0
    for k in tuplis:
            a+=1
            print "Currently parsing %d"%a
            for pair in k:
                    for s in real_squares:
                            tmp = s-pair[0]
                            if tmp != pair[1]:
                                to_test = sorted([pair[1],tmp])
                                #starting here only occurs once per sorted tuplet, should reduce complexity
                                if to_test not in tested:
                                    tested.append(to_test)
                                    tmp_chk = check_2(to_test[0],to_test[1])
                                    if len(tmp_chk) > siz:
                                        check = True
                                        for inst in itertools.combinations(tmp_chk,2):
                                            if len(check_2(inst[0],inst[1])) > siz:
                                                check&=True
                                            else:
                                                check&=False
                                        if check:
                                            print pair, s, tmp


def go2(siz):
    print 'Max: %d'%maxi
    tested = []
    for k in tuplis:
            for pair in k:
                    for s in real_squares:
                            tmp = s-pair[0]
                            if tmp != pair[1]:
                                to_test = sorted([pair[1],tmp])
                                #starting here only occurs once per sorted tuplet, should reduce complexity
                                if to_test not in tested:
                                    tested.append(to_test)
                                    #first test acts as gateway since relatively fast
                                    tmpi = check_2(to_test[0],to_test[1])
                                    if len(tmpi) > siz:
                                        #ulticheck takes longer
                                        ult = ulticheck(tmpi)
                                        if len(ult) > siz:
                                            print to_test
                                    
