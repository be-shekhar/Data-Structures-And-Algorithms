# Below program contains code for Insertion Sort for integers

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and key < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

arr = [6, 5, 3, 1, 8, 7, 2, 4]
# In place sorting, no need to return anything
insertion_sort(arr)
print(arr)

# Lets use the above insertion sort function for sorting custom objects ;)
# Lets create a class that can hold data about a dish

class Dish:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __lt__(self, other):
        return self.price < other.price
    
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

insertion_sort(arr_obj)

print("Array after sorting")
for val in arr_obj:
    print(val)
