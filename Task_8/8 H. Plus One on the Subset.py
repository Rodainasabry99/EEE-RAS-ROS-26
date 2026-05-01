t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    biggest = max(arr)
    smallest = min(arr)
    
    print(biggest - smallest)