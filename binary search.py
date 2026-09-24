n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input("Enter the element: "))
    numbers.append(value)

numbers.sort()
print("Sorted list:", numbers)

key = int(input("Enter the element to search: "))
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) 
    if numbers[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif key < numbers[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("Element not found in the list")
