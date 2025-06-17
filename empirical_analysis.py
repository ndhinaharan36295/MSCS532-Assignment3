import random
from randomized_quick_sort import randomized_quick_sort
import time
import sys
from tabulate import tabulate

sys.setrecursionlimit(6000)

def deterministic_quick_sort(arr):
    def quicksort(arr, low, high):
        # Base case: stop recursion when low >= high
        if low < high:
            # Partitioning array and get the pivot index
            pivot_index = partition(arr, low, high)
            # Recursively sorting the left partition
            quicksort(arr, low, pivot_index - 1)
            # Recursively sorting the right partition
            quicksort(arr, pivot_index + 1, high)

    # Helper function to partition the array
    def partition(arr, low, high):
        # Choosing first element as the pivot
        pivot = arr[low]
        # Initialize the pointer for elements less than the pivot
        i = low + 1
        # Iterate through the array to rearrange/sort elements
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                # Swapping elements to place smaller elements before the pivot
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # Placing the pivot in its correct position
        arr[low], arr[i - 1] = arr[i - 1], arr[low]
        return i - 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]

    # Analysis on Random array
    print(f"\n--- Analysis on Random arrays ---\n")
    results = []
    for size in sizes:
        input_array = [random.randint(1, 10000) for _ in range(size)]

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        deterministic_quick_sort(input_array)
        deterministic_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{randomized_sort_time:.2f} ms", f"{deterministic_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Randomized Quick Sort", "Deterministic Quick Sort"], tablefmt="grid"))


    # Analysis on Sorted array
    print(f"\n--- Analysis on Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size))

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        deterministic_quick_sort(input_array)
        deterministic_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{randomized_sort_time:.2f} ms", f"{deterministic_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Randomized Quick Sort", "Deterministic Quick Sort"], tablefmt="grid"))

    # Analysis on Reverse sorted array
    print(f"\n--- Analysis on Reverse Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size, 0, -1))

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        deterministic_quick_sort(input_array)
        deterministic_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{randomized_sort_time:.2f} ms", f"{deterministic_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Randomized Quick Sort", "Deterministic Quick Sort"], tablefmt="grid"))

    # Analysis on Repeated elements array
    print(f"\n--- Analysis on Repeated Elements arrays ---\n")
    results = []
    for size in sizes:
        input_array = [random.choice([1, 2, 3]) for _ in range(size)]

        start_time = time.time()
        randomized_quick_sort(input_array)
        randomized_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        deterministic_quick_sort(input_array)
        deterministic_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{randomized_sort_time:.2f} ms", f"{deterministic_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Randomized Quick Sort", "Deterministic Quick Sort"], tablefmt="grid"))

