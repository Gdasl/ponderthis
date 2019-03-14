# February

> Assuming this is a result of the fact that only 14 people were used to label the data, one would expect to get 65 different scores. How many people are needed to make the number of possible scores a value that contains all 10 digits, with each digit being used exactly once?

This basically boils down to finding the Farey series of n such that it yields the desired number. One easy way is to first pinpoint the lower and upper boundaries (i.e. n1,n2 for which Farey(n2) < 1000000000 and Farey(n1) > 9999999999. From there it's a straightforward bruteforcing exercise which yields several numbers.
