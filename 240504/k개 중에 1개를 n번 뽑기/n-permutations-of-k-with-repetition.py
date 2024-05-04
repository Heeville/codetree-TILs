from itertools import *

K,N=map(int,input().split())


for w in product(range(1,K+1),repeat=N):
    print(f'{w[0]} {w[1]}')