n = int(input())
lis = [int(x) for  x in input().split()]

lis.sort()
cur = 1
count = 0
for i in lis:
    if cur <= i:
        cur += 1
        count += 1
print(count)
