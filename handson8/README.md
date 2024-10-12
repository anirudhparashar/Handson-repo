For the ith order statistic using quicksort, here's how you can modify your existing quicksort implementation to find the ith smallest element. This is commonly known as the "quickselect" algorithm, which has an average-case time complexity of \(O(n)\).

### Quickselect Algorithm (for ith Order Statistic)

1. **Partition** the array similar to quicksort.
2. After partitioning, if the pivot is at position `i`, return the pivot.
3. If `i` is smaller than the pivot position, recursively search the left part of the array. Otherwise, search the right part.

### Example Code (Python)

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3  # Find the 3rd smallest element
result = quickselect(arr, 0, len(arr) - 1, k - 1)  # k-1 because index starts at 0
print(f"The {k}rd smallest element is {result}")
```

This code will print:  
`The 3rd smallest element is 7`

### Task 2: Stack, Queue, Singly Linked List Using Fixed-size Arrays in C++

Here is an outline of what the implementations might look like.

#### Stack Implementation

```cpp
#include <iostream>
#define MAX 100

class Stack {
    int top;
    int arr[MAX];
    
public:
    Stack() { top = -1; }
    
    bool push(int x) {
        if (top >= (MAX - 1)) {
            std::cout << "Stack Overflow\n";
            return false;
        } else {
            arr[++top] = x;
            return true;
        }
    }
    
    int pop() {
        if (top < 0) {
            std::cout << "Stack Underflow\n";
            return -1;
        } else {
            return arr[top--];
        }
    }
    
    int peek() {
        if (top < 0) {
            std::cout << "Stack is Empty\n";
            return -1;
        } else {
            return arr[top];
        }
    }
    
    bool isEmpty() {
        return (top < 0);
    }
};
```

#### Queue Implementation

```cpp
#include <iostream>
#define MAX 100

class Queue {
    int front, rear;
    int arr[MAX];
    
public:
    Queue() { front = rear = -1; }
    
    bool enqueue(int x) {
        if (rear >= (MAX - 1)) {
            std::cout << "Queue Overflow\n";
            return false;
        } else {
            if (front == -1) front = 0;
            arr[++rear] = x;
            return true;
        }
    }
    
    int dequeue() {
        if (front == -1 || front > rear) {
            std::cout << "Queue Underflow\n";
            return -1;
        } else {
            int val = arr[front];
            front++;
            return val;
        }
    }
    
    bool isEmpty() {
        return (front == -1 || front > rear);
    }
};
```

#### Singly Linked List Implementation

```cpp
#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class SinglyLinkedList {
    Node* head;
    
public:
    SinglyLinkedList() { head = nullptr; }
    
    void append(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }
    
    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
        std::cout << "\n";
    }
};
```
Output of g++ stack_queue_linkedlist.cpp -o main
./main
Stack top: 20
Stack top after pop: 10
Queue front after enqueue: 30
50 60