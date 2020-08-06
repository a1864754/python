n = int(input())
m = {}
i = 1
while i <= n:
    a, b = map(int, input().split())
    m[a] = b
    i += 1
for k in sorted(m, key=m.__getitem__, reverse=True):
    print(k)
    break
