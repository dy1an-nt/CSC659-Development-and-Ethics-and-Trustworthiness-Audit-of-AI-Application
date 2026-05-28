#include <iostream>
#include <memory>
#include <vector>
using namespace std;

void func_fixed_raii() {
    unique_ptr<int[]> arr = make_unique<int[]>(100);
    if (true) return;
}

void func_fixed_vector() {
    vector<int> arr(100);
    if (true) return;
}

int main() {
    func_fixed_raii();
    func_fixed_vector();
    cout << "No leaks (in fixed versions)" << endl;
    return 0;
}
