#include <iostream>
#include <cmath>

class DoublyLinkedList {
public:
    struct Node {
        int key, value;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };
    
    Node* head;
    
    DoublyLinkedList() : head(nullptr) {}

    void insert(int key, int value) {
        Node* newNode = new Node(key, value);
        if (!head) {
            head = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    void remove(int key) {
        Node* temp = head;
        while (temp) {
            if (temp->key == key) {
                if (temp->prev) {
                    temp->prev->next = temp->next;
                }
                if (temp->next) {
                    temp->next->prev = temp->prev;
                }
                if (temp == head) {
                    head = head->next;
                }
                delete temp;
                return;
            }
            temp = temp->next;
        }
    }

    int get(int key) {
        Node* temp = head;
        while (temp) {
            if (temp->key == key) {
                return temp->value;
            }
            temp = temp->next;
        }
        return -1; // Indicates not found
    }

    void clear() {
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
        head = nullptr;
    }

    ~DoublyLinkedList() {
        clear();
    }
};

class HashTable {
private:
    DoublyLinkedList* table;
    int capacity;
    int size;
    const float MAX_LOAD_FACTOR = 0.75;
    const float MIN_LOAD_FACTOR = 0.25;

    // Generic hash function using multiplication method
    int hash(int key) {
        const float A = 0.6180339887; // Fractional part of golden ratio
        return int(capacity * fmod(key * A, 1.0));
    }

    void resize(int new_capacity) {
        DoublyLinkedList* newTable = new DoublyLinkedList[new_capacity];
        for (int i = 0; i < capacity; ++i) {
            DoublyLinkedList::Node* current = table[i].head;
            while (current) {
                int newIndex = hash(current->key);
                newTable[newIndex].insert(current->key, current->value);
                current = current->next;
            }
        }
        delete[] table;
        table = newTable;
        capacity = new_capacity;
    }

    void checkLoadFactor() {
        float loadFactor = float(size) / capacity;
        if (loadFactor > MAX_LOAD_FACTOR) {
            resize(capacity * 2);
        } else if (loadFactor < MIN_LOAD_FACTOR && capacity > 1) {
            resize(capacity / 2);
        }
    }

public:
    HashTable(int init_capacity = 8) : capacity(init_capacity), size(0) {
        table = new DoublyLinkedList[capacity];
    }

    void insert(int key, int value) {
        int index = hash(key);
        table[index].insert(key, value);
        size++;
        checkLoadFactor();
    }

    void remove(int key) {
        int index = hash(key);
        table[index].remove(key);
        size--;
        checkLoadFactor();
    }

    int get(int key) {
        int index = hash(key);
        return table[index].get(key);
    }

    ~HashTable() {
        delete[] table;
    }
};

int main() {
    HashTable ht;
    ht.insert(10, 100);
    ht.insert(20, 200);
    ht.insert(30, 300);

    std::cout << "Get key 20: " << ht.get(20) << std::endl;

    ht.remove(20);
    std::cout << "Get key 20 after removal: " << ht.get(20) << std::endl;

    return 0;
}

