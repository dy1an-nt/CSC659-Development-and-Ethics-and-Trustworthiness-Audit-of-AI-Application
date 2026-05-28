#include <iostream>
#include <cmath>
using namespace std;

void towerOfHanoi(int n, char source, char destination, char auxiliary) {
    if (n == 1) {
        cout << "Move disk 1 from " << source << " to " << destination << endl;
        return;
    }
    towerOfHanoi(n - 1, source, auxiliary, destination);
    cout << "Move disk " << n << " from " << source << " to " << destination << endl;
    towerOfHanoi(n - 1, auxiliary, destination, source);
}

int main() {
    int n = 3;
    cout << "Tower of Hanoi solution for " << n << " disks:" << endl;
    towerOfHanoi(n, 'A', 'C', 'B');
    cout << "\nTotal moves: " << (int)(pow(2, n) - 1) << endl;
    return 0;
}
