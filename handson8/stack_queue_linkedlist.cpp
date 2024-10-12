#include <iostream>
#define MAX 100

// Stack Implementation
class Stack {
    int top;
    int arr[MAX];
public:
    Stack() { top = -1; }
    bool push(int x);
    int pop();
    int peek();
    bool isEmpty();
};

bool Stack::push(int x) {
    if (top >= (MAX - 1)) {
        std::cout << "Stack Overflow\n";
        return false;
    } else {
        arr[++top] = x;
        return true;
    }
}

int Stack::pop() {
    if (top < 0) {
        std::cout << "Stack Underflow\n";
        return -1;
    } else {
        return arr[top--];
    }
}

int Stack::peek() {
    if (top < 0) {
        std::cout << "Stack is Empty\n";
        return -1;
    } else {
        return arr[top];
    }
}

bool Stack::isEmpty() {
    return (top < 0);
}

// Queue Implementation
class Queue {
    int front, rear;
    int arr[MAX];
public:
    Queue() { front = rear = -1; }
    bool enqueue(int x);
    int dequeue();
    bool isEmpty();
};

bool Queue::enqueue(int x) {
    if (rear >= (MAX - 1)) {
        std::cout << "Queue Overflow\n";
        return false;
    } else {
        if (front == -1) front = 0;
        arr[++rear] = x;
        return true;
    }
}

int Queue::dequeue() {
    if (front == -1 || front > rear) {
        std::cout << "Queue Underflow\n";
        return -1;
    } else {
        int val = arr[front++];
        return val;
    }
}

bool Queue::isEmpty() {
    return (front == -1 || front > rear);
}

// Singly Linked List Implementation
class Node {
public:
    int data;
    Node* next;
    Node(int val) { data = val; next = nullptr; }
};

class SinglyLinkedList {
    Node* head;
public:
    SinglyLinkedList() { head = nullptr; }
    void append(int val);
    void display();
};

void SinglyLinkedList::append(int val) {
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

void SinglyLinkedList::display() {
    Node* temp = head;
    while (temp != nullptr) {
        std::cout << temp->data << " ";
        temp = temp->next;
    }
    std::cout << "\n";
}

// Main function to demonstrate usage
int main() {
    // Stack Example
    Stack stack;
    stack.push(10);
    stack.push(20);
    std::cout << "Stack top: " << stack.peek() << "\n";
    stack.pop();
    std::cout << "Stack top after pop: " << stack.peek() << "\n";

    // Queue Example
    Queue queue;
    queue.enqueue(30);
    queue.enqueue(40);
    std::cout << "Queue front after enqueue: " << queue.dequeue() << "\n";

    // Singly Linked List Example
    SinglyLinkedList list;
    list.append(50);
    list.append(60);
    list.display();

    return 0;
}
