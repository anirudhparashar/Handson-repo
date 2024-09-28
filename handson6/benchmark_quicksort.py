import time
import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

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
