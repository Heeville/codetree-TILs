from itertools import *

M,N=map(int,input().split())

for w in combinations(range(1,M+1),N):
    for e in w:
        print(e, end = ' ')
    print()