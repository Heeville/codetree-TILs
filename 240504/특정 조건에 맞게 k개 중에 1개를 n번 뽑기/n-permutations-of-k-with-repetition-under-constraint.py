from itertools import *

K,N=map(int,input().split())

for w in product(range(1,K+1),repeat=N):
    temp=' '.join(map(str, w))
    if '111' or '222' or '333' or '444' not in temp:
        for e in w:
            print(e, end= ' ')
        print()