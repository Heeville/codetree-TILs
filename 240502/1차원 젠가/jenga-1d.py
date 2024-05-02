def remove_blocks(blocks, start, end):
    del blocks[start:end+1]

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

remove_blocks(blocks, s1-1, e1-1)
remove_blocks(blocks, s2-1, e2-1)

print(len(blocks))
for block in blocks:
    print(block)