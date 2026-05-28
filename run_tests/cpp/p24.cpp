#include <iostream>
#include <cstring>
using namespace std;

class MyString {
public:
    char* data;
    MyString(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
    }
    MyString(const MyString& other) {
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
        cout << "[Deep Copy constructor called]" << endl;
    }
    void display() const {
        cout << "Data: " << data << " (address: " << (void*)data << ")" << endl;
    }
    ~MyString() { delete[] data; }
};

int main() {
    MyString original("Hello");
    MyString copy(original);
    cout << "Original: "; original.display();
    cout << "Copy:     "; copy.display();
    strcpy(copy.data, "World");
    cout << "\nAfter modifying copy:" << endl;
    cout << "Original: "; original.display();
    cout << "Copy:     "; copy.display();
    return 0;
}
