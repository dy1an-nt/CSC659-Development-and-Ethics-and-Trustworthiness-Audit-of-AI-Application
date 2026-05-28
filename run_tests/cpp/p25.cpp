#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Person {
    string name;
    int age;
};

int main() {
    vector<Person> people = {
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35},
        {"Diana", 28}
    };
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.age < b.age;
    });
    cout << "Sorted by age (ascending):" << endl;
    for (const auto& p : people) {
        cout << "  " << p.name << " - Age: " << p.age << endl;
    }
    return 0;
}
