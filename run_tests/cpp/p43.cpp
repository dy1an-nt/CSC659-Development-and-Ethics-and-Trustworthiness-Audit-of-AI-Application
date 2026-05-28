#include <iostream>
#include <memory>
using namespace std;

void fix_scope() {
    int x = 10;
    int* p = &x;
    cout << "Value: " << *p << endl;
}

void fix_heap() {
    int* p = new int(10);
    cout << "Value: " << *p << endl;
    delete p;
}

void fix_smart() {
    auto p = make_unique<int>(10);
    cout << "Value: " << *p << endl;
}

int main() {
    fix_scope();
    fix_heap();
    fix_smart();
    return 0;
}
