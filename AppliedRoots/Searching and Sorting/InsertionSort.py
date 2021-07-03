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
insertion_sort(arr)
print(arr)
