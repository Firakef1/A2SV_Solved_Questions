n, s = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]

prefix = [0]*(n+1)

for i in range(len(lis)):
    prefix[i+1] = prefix[i] + lis[i]

one, two = 0 , 1
total = 0
while two < len(prefix):

    if prefix[two]-prefix[one] <= s:
        total += two - one
        two += 1
    else:
        one += 1
print(total)
