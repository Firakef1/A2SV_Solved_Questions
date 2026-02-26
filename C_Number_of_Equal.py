from collections import Counter
n, m = [int(x) for x in input().split()]

lis_one = [int(x) for x in input().split()]
lis_two = [int(x) for x in input().split()]

count = Counter(lis_one)
total = 0

for i in lis_two:
    if i in count:
        total += count[i]

print(total)  
