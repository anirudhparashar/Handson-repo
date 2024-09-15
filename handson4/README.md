# Handson-repo
Let's walk through each of the problems.

### Problem 0: Fibonacci Sequence

The Fibonacci sequence is defined as follows:

```
fib(n) = 0 if n == 0
fib(n) = 1 if n == 1
fib(n) = fib(n-1) + fib(n-2) otherwise
```

**Code Implementation:**

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
```

**Function Call Stack (fib(5)):**

Let's step into the recursive calls:

- `fib(5)` calls `fib(4)` and `fib(3)`
- `fib(4)` calls `fib(3)` and `fib(2)`
- `fib(3)` calls `fib(2)` and `fib(1)`
- `fib(2)` calls `fib(1)` and `fib(0)`
  
Here’s the call stack trace:

```
fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> 1
                 -> fib(0) -> 0
       -> fib(3) -> fib(2) -> fib(1) -> 1
                 -> fib(0) -> 0
```

Result: `fib(5) = 5`.

**Time Complexity:**

The time complexity of the recursive Fibonacci algorithm is **O(2^n)**. This is because each call results in two more recursive calls, leading to exponential growth in function calls.

**Ways to Improve:**

- **Memoization (Top-down Dynamic Programming)**: Cache results of subproblems so that the same subproblem is not solved repeatedly. This reduces the time complexity to **O(n)**.
- **Iterative Approach**: Implement Fibonacci iteratively using a loop, which will also achieve **O(n)** time complexity.

### Problem 1: Merge K Sorted Arrays

Given `K` sorted arrays of size `N`, the task is to merge them while maintaining sorted order.

**Approach:**

We can use a **min-heap (priority queue)** to efficiently merge the arrays. The heap stores the smallest elements from each array, and we repeatedly extract the smallest element from the heap and insert the next element from the same array.

**Code Implementation:**

```python
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
```

**Example Input/Output:**

```python
arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
print(merge_k_sorted_arrays(arrays))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

**Time Complexity:**

The total number of elements is \(K \times N\), and each insertion or deletion from the heap takes **O(log K)** time. Therefore, the time complexity is:

- **O(K * N log K)**

**Ways to Improve:**

- For small `K`, a simple merge without using a heap could be faster.
- Parallelize the merging of arrays if resources allow.

### Problem 2: Remove Duplicates from Sorted Array

Given a sorted array, the task is to remove duplicate elements and return the resulting array.

**Approach:**

Since the array is sorted, we can maintain a pointer to track the last unique element and iterate through the array, only copying over unique elements.

**Code Implementation:**

```python
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
```

**Example Input/Output:**

```python
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))
# Output: [1, 2, 3, 4, 5]
```

**Time Complexity:**

The time complexity is **O(N)**, where \(N\) is the size of the input array, as we are only traversing the array once.

**Ways to Improve:**

- This is already an optimal solution for a sorted array. If the array was not sorted, sorting it first would take **O(N log N)**, which would be the dominating factor in the overall complexity.

---

### Summary of Time Complexities:

- **Problem 0 (Fibonacci):** O(2^n) without optimization.
- **Problem 1 (Merge K Sorted Arrays):** O(K * N log K)
- **Problem 2 (Remove Duplicates):** O(N)
