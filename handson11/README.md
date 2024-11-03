Let's break down your tasks into two parts: 

### Part 1: Implement a Dynamic Array

Here's an implementation of a dynamic array in C++ that behaves like `std::vector`, but only uses C-style arrays for internal storage. We'll support basic operations like insertion, resizing, and accessing elements.

```cpp
#include <iostream>

class DynamicArray {
private:
    int* data;
    int capacity;
    int size;

    void resize(int new_capacity) {
        int* new_data = new int[new_capacity];
        for (int i = 0; i < size; i++) {
            new_data[i] = data[i];
        }
        delete[] data;
        data = new_data;
        capacity = new_capacity;
    }

public:
    DynamicArray() : size(0), capacity(1) {
        data = new int[capacity];
    }

    ~DynamicArray() {
        delete[] data;
    }

    void push_back(int value) {
        if (size == capacity) {
            resize(capacity * 2);
        }
        data[size++] = value;
    }

    int get(int index) const {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    void set(int index, int value) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of range");
        }
        data[index] = value;
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return capacity;
    }
};

int main() {
    DynamicArray arr;

    for (int i = 0; i < 10; i++) {
        arr.push_back(i);
        std::cout << "Added: " << i << ", Size: " << arr.getSize() << ", Capacity: " << arr.getCapacity() << std::endl;
    }

    for (int i = 0; i < arr.getSize(); i++) {
        std::cout << "Element at " << i << ": " << arr.get(i) << std::endl;
    }

    return 0;
}
```

### Explanation of Part 1

- **Dynamic Resizing**: When the array reaches its capacity, it doubles in size by creating a new array of double the capacity and copying the elements from the old array.
- **Methods**:
  - `push_back` to add elements, resizing when necessary.
  - `get` and `set` to retrieve and modify elements.
  - `getSize` and `getCapacity` to retrieve current size and capacity of the array.

### Part 2: Amortized Runtime Analysis of Insertions

When inserting \( n \) elements into a dynamic array that doubles its capacity upon reaching the limit, we can use two methods to analyze the amortized runtime: the **aggregate method** and the **accounting method**.

#### (a) Aggregate Method

The **aggregate method** calculates the total work required to insert \( n \) elements, then finds the average cost per insertion.

1. **Cost Analysis**:
   - When inserting an element, it costs **1 unit** if there's space.
   - If the array is full, we double its size, which requires **copying all elements** to the new array. If capacity doubles each time, the cost for doubling is proportional to the current capacity.
   
2. **Total Work for \( n \) Insertions**:
   - Each time we double, we perform work proportional to the new capacity. So, the total work \( W(n) \) for inserting \( n \) elements is:
     \[
     W(n) = 1 + 2 + 4 + 8 + \dots + n = 2n - 1
     \]
   - **Amortized Cost**: The amortized cost per insertion is the total work divided by the number of insertions:
     \[
     \frac{W(n)}{n} = \frac{2n - 1}{n} \approx 2
     \]
   - **Result**: The amortized cost for each insertion is \( O(1) \).

#### (b) Accounting Method

In the **accounting method**, we assign a "charge" to each operation to pay for future costly operations, such as resizing.

1. **Assign Cost Per Operation**:
   - Suppose we charge **3 units** for every insertion:
     - **1 unit** is used for the insertion itself.
     - The remaining **2 units** are saved for future resizing.

2. **Using Saved Units**:
   - Each time we double the array, the resizing cost for copying all elements is covered by the extra units saved from previous insertions.

3. **Result**: By setting aside these saved units, we ensure that each operation has a constant amortized cost of \( O(1) \).
