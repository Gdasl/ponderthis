# January Ponder this

## Problem statement

> Alice and Bob are playing the following game: they start from a number N and each one of them in his or her turn (Alice starts) divides N by any divisor that is either a prime or a product of several distinct prime numbers. The winner is the one who gets to one - thus leaving the other player with no legal move. 
To define the initial N, Alice chooses a number a from a set A, and a number b from a set B. The game is played with N=a+b. Charlie knows that Alice will start, and he wants to let Bob win. He does that by fixing the sets A and B.

>He can do that, for example, by choosing A=[3,99] and B=[1,22]. (Why?)

>Your challenge, this month, is to help Charlie find sets A and B with at least four different numbers each, that will allow Bob to win.
Bonus '*' for solutions with more than 4 elements in the set B.

[Link](http://www.research.ibm.com/haifa/ponderthis/challenges/January2019.html) to description.
The basic idea was to find is that all possible sums between A and B have to be perfect squares, since this results in having N = Prod(i^k_i) for al prime factors i of N and k is always a multiple of 2. This guarantees that the second person playing the game will always win.

## Approaches
### Python

#### First version
I started naively, not noticing that N was always going to be square, looking for solutions with a small N. Basically a brute-force exercise using the following algorithm:

1) Create all separate tuples [a,b,c,d] for a..d <= 10
2) Use first list toc reate all possible combinations of 2 non-equal sets
3) Create a list of all possible sums
4) Check for each sum if it the prime factors are multiples of 2

Needless to say this proved to be inefficient at best. I then reversed the problem and realized the connection with the squares.

#### Second version

I quickly realized that another way was to decompose the squares in their possible sums. For example `4` can only be `1+3`. Furthermore, I realized that given `[a,b]`, in order to find an element of the opposite set, I had to find i s.t. `a + i` and `b+i`is a square. For each pair I subsequently cycled through each square in my precalculated list (!) and checked if such an i existed for each combination. To recapitulate:

1) Precalculate all squares up to a given N
2) For each square create a set of its possible sums
3) For each sum, take the first number
4) For each square, substract the first number
5) Check if there are at least 4 distinct i < N**2 that satisfiy the equation `p_i - t_k[0] + i` in squares and `t_k[1] + i` in squares, whereby `p_i` is a square and `t_k` is a sum decomposition of a square

I am honestly blushing writing this. It's ridiculous and takes exponential time, even using dp. 

#### Third version (Final)

At this point I was compiling everything to C using shedskin to make it run faster but given the exponential nature of the task it absolutely didn't matter. Running it with Squares up to 100 (max i = 10000) barely made it to 50 after 48h running. I then went another approach using linear solving. That didn't pan out either and by that point, January was over. I wento on with my life, solved the February challenge and decided to revisit January. That's when I realized the two largest flaws: 

- not checking for trivial solutions (i.e. a[0] = 0)
- looping through all i <= N**2

Basically, if `a + i` is a square and `b + i` is a square, taking the set of `[s_i - a]` and of `[s_i - b]` for all s_i in squares and interescting the sets instantly gives me the list of `i`. This approach as well as assuming that `a[0] = 0` allowed me to find > 100 solutions in a few minutes after compiling to C.

Final algorithm:

1) Precalculate list of squares up to N
2) Assume `a[0] = 0` s.t. all elements in B have to be squares
3) Take all tuplets `(k,j)` where k and j are squares and k != j
4) Find all `i` s.t. `i+k` and `j+i` are also squares
5) Make a list of all possible sets of 4 among the found `i`
6) For each quadruplet test all possible combinations `(a,b)` to make sure there are at least 4 `i` satisfying `a+i` and `b+i` are both squares and that the intersection of all resulting sets has at leas length 4

### Z3

Making this short: z3 is an excellent linear solver. The basic idea was to dissect the problem into discrete constraints and let it run. The approach works well if the length of the sets is >=3 but barfs above that. Linear solvers just don't do well with multiplication, especially when the possible values are so many.
