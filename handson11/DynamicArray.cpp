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
