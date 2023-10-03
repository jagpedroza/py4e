largest = None
smallest = None
numbers = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        numbers.append(int(num))
        largest = max(numbers)
        smallest= min(numbers)
        
    except ValueError:
        print("Invalid input")
        

print("Maximum is", largest)
print("Minimum is", smallest)