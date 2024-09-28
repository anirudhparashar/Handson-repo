Here's an outline of how to implement the quicksort algorithm with both random and non-random pivot selection, along with the benchmarking plan and the steps to derive the average runtime complexity of non-random quicksort.

### 1. Implementing Quicksort

**Non-random pivot version:**

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

**Random pivot version:**

```python
import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot selection
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + middle + quicksort_random(right)
```

### 2. Benchmarking the Non-Random Pivot Version

We can generate inputs for different cases and collect benchmarks for varying input sizes \( n \). Here’s how you can prepare the inputs for each case:

- **Best Case**: Quicksort’s best case occurs when the pivot divides the array perfectly into two equal halves at each step. This happens when the array is already balanced. One way to achieve this is to use a pre-sorted array in the format of a balanced binary tree.

- **Worst Case**: The worst case occurs when the pivot is always the smallest or largest element. A sorted or reverse-sorted array will represent this scenario.

- **Average Case**: The average case occurs when the input array has no particular order (i.e., elements are uniformly random).

**Python benchmarking code using `time` library:**

```python
import time
import random

def benchmark_quicksort(arr_sizes, case_type="average"):
    times = []
    
    for n in arr_sizes:
        if case_type == "best":
            # Generate a balanced array (simulate best case)
            arr = list(range(n))
        elif case_type == "worst":
            # Generate a sorted array (worst case)
            arr = list(range(n, 0, -1))
        else:
            # Generate a random array (average case)
            arr = [random.randint(0, n) for _ in range(n)]
        
        start_time = time.time()
        quicksort(arr)
        times.append(time.time() - start_time)
    
    return times
```

**Plotting Results:**
You can collect and plot the results using `matplotlib`.

```python
import matplotlib.pyplot as plt

def plot_benchmark(arr_sizes, best_times, worst_times, avg_times):
    plt.plot(arr_sizes, best_times, label='Best Case')
    plt.plot(arr_sizes, worst_times, label='Worst Case')
    plt.plot(arr_sizes, avg_times, label='Average Case')
    
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Performance')
    plt.legend()
    plt.show()

# Example usage
arr_sizes = [100, 500, 1000, 5000, 10000]
best_times = benchmark_quicksort(arr_sizes, case_type="best")
worst_times = benchmark_quicksort(arr_sizes, case_type="worst")
avg_times = benchmark_quicksort(arr_sizes, case_type="average")

plot_benchmark(arr_sizes, best_times, worst_times, avg_times)
```

### 3. Mathematical Derivation of Average Runtime Complexity

The average-case runtime complexity of quicksort can be derived as follows:

- At each recursive step, we pick a pivot that divides the array into two parts.
- On average, the pivot splits the array into two approximately equal halves.
  
At each level of recursion:
- The number of comparisons is proportional to the size of the array, i.e., \( O(n) \).
  
The depth of the recursion tree is \( O(\log n) \) because each time we are halving the array size (on average). Thus, the total number of comparisons (the runtime) in the average case is the product of the number of levels and the comparisons per level, which results in:

\[
T(n) = O(n \log n)
\]

This is the average-case time complexity of quicksort.

---
