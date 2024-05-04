from itertools import *

K,N=map(int,input().split())

for w in product(range(1,K+1),repeat=N):
    temp=''.join(map(str, w))
    if '111' in temp:
        continue
    elif '222' in temp:
        continue
    elif '333' in temp:
        continue
    elif '444' in temp:
        continue
    for e in w:
        print(e, end= ' ')
    print()