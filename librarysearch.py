
book_ids = [101, 105, 110, 115]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

search_id = int(input("Enter Book ID to search: "))

result = binary_search(book_ids, search_id)

if result != -1:
    print(f"Book ID {search_id} is present in the library.")
    print(f"Index Number: {result}")
else:
    print(f"Book ID {search_id} is NOT present in the library.")