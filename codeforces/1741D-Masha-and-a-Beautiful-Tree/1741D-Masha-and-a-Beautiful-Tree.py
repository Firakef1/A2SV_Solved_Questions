def merge_sort(lis):
    
    if len(lis) == 1:
        return lis

    mid = len(lis)//2

    one = merge_sort(lis[:mid])
    two = merge_sort(lis[mid:])
    # print(one, two)
    if not one or not two:
        return False
    
    return merge(one, two)

def merge(one, two):
    global ans
    # print(one, two)
    if not one or not two:
        return False
    
    out = []

    if one[0] < two[0]:
        out.extend(one)
        out.extend(two)
    else:
        ans += 1
        out.extend(two)
        out.extend(one)
    
    # print(out)
    if is_sorted(out):
        return out

    return False

def is_sorted(lis):
    
    for i in range(1, len(lis)):
        if lis[i-1] >= lis[i]:
            return False
    
    return True



t = int(input())

for _ in range(t):
    n = int(input())
    lis = [int(x) for x in input().split()]
    ans = 0
    if n == 1:
        print(0)
    elif merge_sort(lis):
        print(ans)
    else:
        print(-1)