import random

def randomized_quick_sort(arr):
    # Base case: stop recursion when low >= high
    def quicksort(arr, low, high):
        if low < high:
            # Partitioning the array using a randomized pivot
            pivot_index = randomized_partition(arr, low, high)
            # Recursively sorting the left partition
            quicksort(arr, low, pivot_index - 1)
            # Recursively sorting the right partition
            quicksort(arr, pivot_index + 1, high)

    # Helper function to partition the array using a randomized pivot
    def randomized_partition(arr, low, high):
        # Choosing a random index for the pivot
        rand_index = random.randint(low, high)
        # Swap the pivot element with the last element
        arr[high], arr[rand_index] = arr[rand_index], arr[high]
        # Setting the pivot element
        pivot = arr[high]
        # Initialize the pointer for elements less than the pivot
        i = low - 1
        # Iterate through the array to rearrange/sort elements
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                # Swap elements to place smaller elements before the pivot
                arr[i], arr[j] = arr[j], arr[i]
        # Place the pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    # Test cases

    # Empty array
    empty_array = []
    # Random array
    random_array = [13, 21, 4, 11, 15, 19, 12]
    # Sorted array
    sorted_array = [11, 12, 13, 14, 15]
    # Reverse-sorted
    reverse_sorted_array= [15, 14, 13, 12, 11]
    # Repeated elements
    repeated_elements = [12, 13, 12, 13, 12, 13]

    print("--- Randomized Quick Sort ---\n")

    print(f"Testing on Empty array: {empty_array}")
    output_arr = randomized_quick_sort(empty_array)
    print(f"Output = {output_arr}\n")

    print(f"Testing on Random array: {random_array}")
    output_arr = randomized_quick_sort(random_array)
    print(f"Output = {output_arr}\n")

    print(f"Testing on Sorted array: {sorted_array}")
    output_arr = randomized_quick_sort(sorted_array)
    print(f"Output = {output_arr}\n")

    print(f"Testing on Reverse-Sorted array: {reverse_sorted_array}")
    output_arr = randomized_quick_sort(reverse_sorted_array)
    print(f"Output = {output_arr}\n")

    print(f"Testing on Repeated Elements array: {repeated_elements}")
    output_arr = randomized_quick_sort(repeated_elements)
    print(f"Output = {output_arr}\n")

