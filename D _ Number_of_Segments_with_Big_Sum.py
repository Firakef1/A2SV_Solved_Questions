n, s = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]

if sum(lis) < s:
    print(0)
    exit()

one = 0
current_sum = 0
total = 0

for two in range(n):
    current_sum += lis[two]
    
    while current_sum >= s:

        total += (n - two) 
        
        current_sum -= lis[one]
        one += 1

print(total)
