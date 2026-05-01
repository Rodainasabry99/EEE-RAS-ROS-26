t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr[0] == arr[1] or arr[0] == arr[2]:
        normal = arr[0]
    else:
        normal = arr[1]

    for i in range(n):
        if arr[i] != normal:
            print(i + 1)
            