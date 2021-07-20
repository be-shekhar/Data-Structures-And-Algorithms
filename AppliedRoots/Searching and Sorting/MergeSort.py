# Below program contains code for Merge Sort for integers

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print("Left:", left)
        mergeSort(left)
        print("Right:", right)
        mergeSort(right)
        print("Array:", arr, left, right)
        merge(arr, left, right)
        print("Sorted array:", arr)

arr = [6, 5, 3, 1]
mergeSort(arr)
print(arr)

# Lets use the above merge sort function for sorting custom objects ;)
# Lets create a class that can hold data about a dish

class Dish:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __le__(self, other):
        return self.price <= other.price
    
    def __str__(self):
        return "Name: " + str(self.name) + " Price: " + str(self.price)

    
arr_obj = [
    Dish(name='Dosa', price=20),
    Dish(name='Biryani', price=100),
    Dish(name='Soup', price=50),
    Dish(name='Paneer Masala', price=250),
    Dish(name='Coffee', price=10)
]

print("Array before sorting")
for val in arr_obj:
    print(val)

mergeSort(arr_obj)

print("Array after sorting")
for val in arr_obj:
    print(val)
