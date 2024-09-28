import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot selection
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + middle + quicksort_random(right)