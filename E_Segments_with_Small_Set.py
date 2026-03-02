n, k = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]

counts = {}
u_count = 0
left = 0
total = 0

for right in range(n):
    val_r = lis[right]
    if counts.get(val_r, 0) == 0:
        u_count += 1
    counts[val_r] = counts.get(val_r, 0) + 1

    while u_count > k:
        val_l = lis[left]
        counts[val_l] -= 1
        if counts[val_l] == 0:
            u_count -= 1
        left += 1

    total += (right - left + 1)

print(total)
