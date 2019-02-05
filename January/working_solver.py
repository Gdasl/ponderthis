import itertools

maxi = 3000
target = 4
def squares(n):
    return [i**2 for i in xrange(1,n+1)]

def ulticheck(tu,rs):
    arri = []
    for i in itertools.combinations(tu,2):
        tmp_arri = check_3(i[0],i[1],rs)
        #print i[0], i[1], tmp_arri
        if len(tmp_arri) < target:
            
            return
        arri.append(tmp_arri)
        
    if len(arri) > 1:
        result = set(arri[0])
        for s in arri[1:]:
            result.intersection_update(s)
            if len(result) < target:
                return
        print result
        return result

dp = {}

def check_3(a,b,rs):
    if dp.get((a,b)):
        return dp[(a,b)]
    if dp.get((b,a)):
        return dp[(b,a)]
    a1 = set([i - a for i in rs])
    b1 = set([i-b for i in rs])
    
    tomp = list(a1.intersection(b1))
    dp[(a,b)] = tomp
    return tomp
    


a = 0

sq = squares(maxi)

print 'hello'
#print ulticheck([9, 28224, 419904, 3968064],sq)

tmp = check_3(0,47952,sq)
print tmp

##for i in itertools.combinations(tmp,4):
##    print ulticheck(i,sq)

for j in sq:
    print j
    for k in sq:
        if k != j:
            #print k
            tmpi = check_3(j,k,sq)
            if len(tmpi) > (target-1):
                for i in itertools.combinations(tmpi,4):
                    if ulticheck(i,sq) is not None:
                        print ulticheck(i,sq), ulticheck(ulticheck(i,sq),sq)


