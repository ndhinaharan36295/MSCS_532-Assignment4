import random
from heap_sort import Heap
import time
import sys
from tabulate import tabulate

sys.setrecursionlimit(6000)

# Quick Sort implementation
class QuickSort:
    def quicksort(self, arr):
        # Starting the quick sort process
        self.sort(arr, 0, len(arr) - 1)

    def sort(self, arr, low, high):
        if low < high:
            # Partitioning the array
            pivot_index = self.partition(arr, low, high)
            # Recursively sorting the left partition
            self.sort(arr, low, pivot_index - 1)
            # Recursively sorting the right partition
            self.sort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
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

# Quick sort implementation with median-of-three pivot selection
class QuickSortMedianOfThree(QuickSort):
    def quicksort(self, arr):
        # Starting the quick sort process
        self.sort(arr, 0, len(arr) - 1)

    def sort(self, arr, low, high):
        if low < high:
            # Partitioning the array
            pivot_index = self.partition(arr, low, high)
            # Recursively sorting the left partition
            self.sort(arr, low, pivot_index - 1)
            # Recursively sorting the right partition
            self.sort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        # Setting the pivot element using median-of-three strategy
        pivot = self.choose_pivot(arr, low, high)
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

    # choose pivot with Median-of-Three method
    def choose_pivot(self, arr, low, high):
        # Select pivot as median of first, middle, last elements
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        return mid

# Merge Sort implementation
class MergeSort:
    def merge(self, left, right):
        merged = []
        i = j = 0

        # Merge elements in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr

        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = self.mergesort(arr[:mid])
        right_half = self.mergesort(arr[mid:])

        # Merge the sorted halves
        return self.merge(left_half, right_half)


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000]

    heap_sorter = Heap()
    merge_sorter = MergeSort()
    quick_sorter = QuickSort()

    # Analysis on Random array
    print(f"\n--- Analysis on Random arrays ---\n")
    results = []
    for size in sizes:
        input_array = [random.randint(1, 10000) for _ in range(size)]

        start_time = time.time()
        heap_sorter.heapsort(input_array)
        heap_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        merge_sorter.mergesort(input_array)
        merge_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        quick_sorter.quicksort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{merge_sort_time:.2f} ms", f"{heap_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Quick Sort", "Merge Sort", "Heap Sort"], tablefmt="grid"))


    # Analysis on Sorted array
    print(f"\n--- Analysis on Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size))

        start_time = time.time()
        heap_sorter.heapsort(input_array)
        heap_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        merge_sorter.mergesort(input_array)
        merge_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        quick_sorter.quicksort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{merge_sort_time:.2f} ms", f"{heap_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Quick Sort", "Merge Sort", "Heap Sort"], tablefmt="grid"))

    # Analysis on Reverse sorted array
    print(f"\n--- Analysis on Reverse Sorted arrays ---\n")
    results = []
    for size in sizes:
        input_array = list(range(size, 0, -1))

        start_time = time.time()
        heap_sorter.heapsort(input_array)
        heap_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        merge_sorter.mergesort(input_array)
        merge_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        start_time = time.time()
        quick_sorter.quicksort(input_array)
        quick_sort_time = (time.time() - start_time) * 1000  # in milliseconds

        results.append([size, f"{quick_sort_time:.2f} ms", f"{merge_sort_time:.2f} ms", f"{heap_sort_time:.2f} ms"])

    # Print results as a table
    print(tabulate(results, headers=["Array Size", "Quick Sort", "Merge Sort", "Heap Sort"], tablefmt="grid"))
