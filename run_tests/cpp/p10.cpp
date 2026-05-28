#include <iostream>
using namespace std;

int main() {
    int a = 0, b = 1;
    cout << "First 10 Fibonacci numbers: ";
    for (int i = 0; i < 10; i++) {
        cout << a << " ";
        int next = a + b;
        a = b;
        b = next;
    }
    cout << endl;
    return 0;
}
