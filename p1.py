#def mystery(arr):
#    for i in range(len(arr)):
#        for j in range(i, len(arr)):
#            if arr[i] > arr[j]:
#                arr[i], arr[j] = arr[j], arr[i]
#    return arr            


# Implementación de QuickSort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(quicksort(arr))