import heapq

def merge_k_sorted_arrays(arrays):
    merged_array = []
    min_heap = []
    
    # Insert the first element of each array along with the array index and element index
    for i in range(len(arrays)):
        heapq.heappush(min_heap, (arrays[i][0], i, 0))
    
    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        
        # If there is a next element in the same array, push it to the heap
        if element_idx + 1 < len(arrays[array_idx]):
            next_value = arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, array_idx, element_idx + 1))
    
    return merged_array
