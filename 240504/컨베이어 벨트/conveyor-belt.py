def rotate(upper, lower):
    gounder=upper[-1]
    goup=lower[-1]
    upper = [goup] + upper[:-1]
    lower = [gounder] + lower[:-1]
    return upper, lower

n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))


for _ in range(t):
    upper, lower = rotate(upper, lower)


print(' '.join(map(str, upper)))
print(' '.join(map(str, lower)))