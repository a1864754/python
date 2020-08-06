a = int(input())
one = input().split()
one = list(map(int, one))
two = []
sum1 = 0
for i in one:
    two.append([i, 1])

a = 0
while a < len(one):
    if a == 0:
        if two[a][0] > two[a + 1][0]:
            sum1 += 1
            a += 1
            continue
    elif a == len(one) - 1:
        if two[a][0] > two[a - 1][0]:
            sum1 += 1
            a += 1
            break
    elif two[a][0] > two[a + 1][0] and two[a][0] > two[a - 1][0]:
        two[a][0] += 1
        sum1 += 1
        a += 1
    a += 1
for i in two:
    print(i)
    sum1 += i[1]
print(sum1)
