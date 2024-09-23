class MinHeap:
    def __init__(self, data=None):
        """Initialize the heap."""
        self.heap = []
        if data:
            self.build_min_heap(data)

    def build_min_heap(self, data):
        """Build a min-heap from an initial list of data."""
        self.heap = data[:]
        # Build heap (start from the last parent and heapify down)
        for i in range((len(self.heap) - 2) >> 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        """Ensure the heap property is maintained starting from index i."""
        size = len(self.heap)
        left = (i << 1) + 1
        right = (i << 1) + 2
        smallest = i

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def push(self, item):
        """Add an item to the heap."""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        """Move the item at index i up to restore the heap property."""
        parent = (i - 1) >> 1
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) >> 1

    def pop(self):
        """Remove and return the smallest item from the heap."""
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()  # Directly return the last item if it's the only one
        
        root = self.heap[0]
        # Move the last element to the root and heapify down
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self.heapify(0)  # Re-heapify starting from the root
        return root

    def peek(self):
        """Return the smallest item without removing it."""
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap)


# Demonstration of heap functionality
if __name__ == "__main__":
    # Example 1: Building the heap from a list
    data = [9, 4, 7, 1, 10, 3]
    heap = MinHeap(data)
    print("Initial min-heap:", heap)

    # Example 2: Push elements into the heap
    heap.push(2)
    heap.push(15)
    print("Heap after pushes:", heap)

    # Example 3: Peek at the root (minimum element)
    print("Peek root:", heap.peek())

    # Example 4: Pop elements from the heap
    print("Pop root:", heap.pop())
    print("Heap after pop:", heap)

    # Example 5: Continue popping elements
    while heap.heap:
        print("Pop root:", heap.pop())
        print("Heap after pop:", heap)
