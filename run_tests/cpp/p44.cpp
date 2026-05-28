#include <iostream>
#include <cstring>
using namespace std;

class MyString {
private:
    char* data;
    size_t length;
public:
    MyString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "[Constructor] \"" << data << "\"" << endl;
    }
    ~MyString() {
        cout << "[Destructor] \"" << data << "\"" << endl;
        delete[] data;
    }
    MyString(const MyString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "[Copy Constructor] \"" << data << "\"" << endl;
    }
    MyString& operator=(const MyString& other) {
        if (this == &other) return *this;
        delete[] data;
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "[Copy Assignment] \"" << data << "\"" << endl;
        return *this;
    }
    const char* c_str() const { return data; }
    size_t size() const { return length; }
};

int main() {
    MyString s1("Hello");
    MyString s2 = s1;
    MyString s3("World");
    s3 = s1;
    cout << "\nValues: " << s1.c_str() << ", " << s2.c_str() << ", " << s3.c_str() << endl;
    return 0;
}
