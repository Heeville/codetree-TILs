from itertools import *

n=int(input())

for i in permutations(range(1,n+1),n):
    for w in i:
        print(w, end = ' ')
    print()