from difflib import SequenceMatcher
import operator
import timeit
y = []
z = []
x = [1,2,3,4,5]

for i in x:
    y.append(x[:len(x)-1])
    z.append(x[4])

print y
print z
