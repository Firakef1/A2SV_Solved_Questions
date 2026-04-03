from bisect import bisect_left

t = int(input())

def is_sorted(lis):
    for i in range(1, len(lis)):
        if lis[i] < lis[i-1]:
            return False
    return True

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    lis_a = [int(x) for x in input().split()]
    lis_b = [int(x) for x in input().split()]
    lis_b.sort()
    
    option1 = lis_a[0]
    option2 = lis_b[0] - lis_a[0]
    lis_a[0] = min(option1, option2)

    possible = True
    for i in range(1, n):
        v_orig = lis_a[i]
        
 
        target = lis_a[i-1] + lis_a[i]
        index = bisect_left(lis_b, target)
        
        v_flip = float('inf')
        if index < m:
            v_flip = lis_b[index] - lis_a[i]

        res = float('inf')
        if v_orig >= lis_a[i-1]:
            res = min(res, v_orig)
        if v_flip >= lis_a[i-1]:
            res = min(res, v_flip)
            
        if res == float('inf'):
            print("NO")
            possible = False
            break
        
        lis_a[i] = res
        
    if possible:
        
        print("YES")