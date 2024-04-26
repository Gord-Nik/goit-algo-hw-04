import timeit
import random

# Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        # Correct comparison in merging logic
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Prepare arrays of different sizes
sizes = [100, 1000, 10000]
arrays = {size: [random.randint(1, 10000) for _ in range(size)] for size in sizes}

# Time the algorithms
def time_algorithm(algorithm, arr):
    arr_copy = arr.copy()  # Ensure the array is fresh for each test
    return timeit.timeit(lambda: algorithm(arr_copy), number=10)

# Execute and record results
results = {}
for size in sizes:
    results[size] = {
        'Insertion Sort': time_algorithm(insertion_sort, arrays[size]),
        'Merge Sort': time_algorithm(merge_sort, arrays[size]),
        'Timsort': time_algorithm(sorted, arrays[size])
    }

# Display results
for size, timings in results.items():
    print(f"Array size: {size}")
    for algo, timing in timings.items():
        print(f"{algo}: {timing:.5f} seconds")