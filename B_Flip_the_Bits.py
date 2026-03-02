t = int(input())

for _ in range(t):
    n = int(input())

    a = input()+"0"
    b = input()+"0"

    state = 0

    for i in range(n):
        state += (a[i] == "1") - (a[i] == "0")

        if (a[i] == b[i]) !=  (a[i+1] == b[i+1]) and state != 0:
            print("NO")
            break
    else:
        print("YES")
