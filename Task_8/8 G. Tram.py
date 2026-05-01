n = int(input())

passengers = 0
capacity = 0

for i in range(n):
    a, b = map(int, input().split())
    
    passengers = passengers - a + b
    
    if passengers > capacity:
        capacity = passengers

print(capacity)