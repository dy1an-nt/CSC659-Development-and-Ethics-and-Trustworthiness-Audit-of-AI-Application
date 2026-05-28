#include <iostream>
using namespace std;

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    cout << "Array elements: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
