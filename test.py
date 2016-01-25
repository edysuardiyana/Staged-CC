from difflib import SequenceMatcher
import operator
import timeit

x = timeit.default_timer()
a = [5,6,7,8,1,2,3,4]
b = [1,2,3,3,0]

index, max_val = max(enumerate(b),key=operator.itemgetter(1))

print index
print max_val

y = timeit.default_timer()
print (y-x)

print x

for i in range(10):
    for j in range(20):

        print "This is git testing"
