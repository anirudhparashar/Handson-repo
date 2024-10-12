def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3  # Find the 3rd smallest element
result = quickselect(arr, 0, len(arr) - 1, k - 1)  # k-1 because index starts at 0
print(f"The {k}rd smallest element is {result}")
