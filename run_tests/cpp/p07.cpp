#include <iostream>
using namespace std;

int findLargest(int a, int b, int c) {
    int largest;
    if (a >= b && a >= c) {
        largest = a;
    } else if (b >= a && b >= c) {
        largest = b;
    } else {
        largest = c;
    }
    return largest;
}

int main() {
    int x, y, z;
    cout << "Enter three numbers: ";
    cin >> x >> y >> z;
    cout << "The largest is: " << findLargest(x, y, z) << endl;
    return 0;
}
