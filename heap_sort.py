class Heap:
    def max_heapify(self, arr, i, heap_size):
        # Calculate the indices of the left and right children
        left = 2 * i
        right = 2 * i + 1

        # Check if the left child exists and is greater than the current node
        if left <= heap_size and arr[left] > arr[i]:
            # If yes, update largest to be the left child
            largest = left
        else:
            # If not, the current node is still the largest
            largest = i

        # Check if the right child exists and is greater than the current largest
        if right <= heap_size and arr[right] > arr[largest]:
            # If yes, update largest to be the right child
            largest = right

        # If the largest is not the current node, swap and continue heapify-ing
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest, heap_size)

    def build_max_heap(self, arr, heap_size):
        # Build a max heap by heapify-ing all non-leaf nodes
        for i in range(heap_size // 2, 0, -1):
            self.max_heapify(arr, i, heap_size)

    def heapsort(self, arr):
        # Adding a dummy element at index 0 for 1-based indexing
        arr = [None] + arr
        heap_size = len(arr) - 1

        # Build the max heap
        self.build_max_heap(arr, heap_size)

        # Perform heap sort by repeatedly extracting the maximum element
        for i in range(len(arr) - 1, 1, -1):
            # Swap the root with the last element
            arr[1], arr[i] = arr[i], arr[1]
            # Reduce the heap size
            heap_size -= 1
            # Restore the heap property
            self.max_heapify(arr, 1, heap_size)

        # Remove dummy element and return sorted array
        return arr[1:]

# Example usage
if __name__ == "__main__":
    print("--- Heap Sort Execution ---\n")

    data = [12, 21, 13, 5, 8, 7]
    print("Initial Random array:", data)

    heap = Heap()

    sorted_data = heap.heapsort(data)
    print("Sorted array:", sorted_data)

    data = [11, 12, 13, 14, 15, 16]
    print("\nInitial Sorted array:", data)

    sorted_data = heap.heapsort(data)
    print("Sorted array:", sorted_data)

    data = [16, 15, 14, 13, 12, 11]
    print("\nInitial Reverse-Sorted array:", data)

    sorted_data = heap.heapsort(data)
    print("Sorted array:", sorted_data)
