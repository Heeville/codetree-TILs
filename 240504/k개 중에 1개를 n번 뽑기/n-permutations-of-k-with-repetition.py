answer=[]

K,N=map(int,input().split())

def choose(curr_num):

    if curr_num == N+1:
        print(*answer)
        return

    for i in range(1,K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()


choose(1)