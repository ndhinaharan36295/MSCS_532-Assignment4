# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

## Overview

This project demonstrates the implementation and analysis of two key applications of heap data structures:

1. **Heapsort** – An efficient in-place sorting algorithm using a max-heap.
2. **Priority Queue** – A min-heap-based priority queue supporting task scheduling with dynamic priorities.

The code is written in Python and includes detailed performance analysis, theoretical complexity discussion, and simulation-ready components.

---

## 📁 Contents

- `heap_sort.py` – Heapsort algorithm using a max-heap (1-based indexing, CLRS style).
- `priority_queue.py` – Min-heap-based priority queue with `insert`, `extract_min`, and `decrease_key`.
- `empirical_analysis.py` – Script comparing Heapsort with quicksort & mergesort algos.

---

## ⚙️ How to Run the Code

### Requirements
- Python 3.7 or higher
- No external libraries required (only `time` and optionally `matplotlib` for benchmarking)

### Running Heapsort
```
python3 heap_sort.py
```

### Running Empirical comparison
```
python3 empirical_analysis.py
```

### Running Priority Queue
```
python3 priority_queue.py
```
