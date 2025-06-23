class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # For min-heap comparison

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            return None
        min_task = self.heap[0]
        last_task = self.heap.pop()
        if self.heap:
            self.heap[0] = last_task
            self._heapify(0)
        return min_task

    def decrease_key(self, index, new_priority):
        if new_priority >= self.heap[index].priority:
            return  # new priority is not lower
        self.heap[index].priority = new_priority
        self._bubble_up(index)

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify(smallest)

    def __repr__(self):
        return f"{self.heap}"

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task("Task-1", 5, 0, 10))
    pq.insert(Task("Task-2", 3, 1, 7))
    pq.insert(Task("Task-3", 8, 2, 5))

    print("--- Initial Queue ---\n")
    print(pq)

    print("\n--- Extracted Min Element ---\n")
    print(pq.extract_min())

    print("\n--- After Extraction ---\n")
    print(pq)

    # Decrease key of T3 (now at index 1 or 0 depending on heap state)
    pq.decrease_key(0, 1)  # Assuming index is known
    print("\n--- After Decrease Key ---\n")
    print(pq)
