def remove_duplicates(arr):
    if not arr:
        return []
    
    # Pointer for the next unique element
    unique_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    
    # Slice the array up to the last unique element
    return arr[:unique_index + 1]
