first = True

while True:
    num = int(input("Enter number (-1 to stop): "))
    
    if num == -1:
        break
    
    if first:
        largest = smallest = num
        first = False
    else:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

if first:
    print("No numbers entered")
else:
    print("Largest:", largest)
    print("Smallest:", smallest)