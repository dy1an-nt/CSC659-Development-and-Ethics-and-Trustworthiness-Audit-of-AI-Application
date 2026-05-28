#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class SinglyLinkedList {
private:
    Node* head;
public:
    SinglyLinkedList() : head(nullptr) {}
    void insertAtHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }
    void display() const {
        Node* current = head;
        cout << "List: ";
        while (current != nullptr) {
            cout << current->data;
            if (current->next) cout << " -> ";
            current = current->next;
        }
        cout << " -> NULL" << endl;
    }
    ~SinglyLinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
};

int main() {
    SinglyLinkedList list;
    list.insertAtHead(30);
    list.insertAtHead(20);
    list.insertAtHead(10);
    list.display();
    return 0;
}
