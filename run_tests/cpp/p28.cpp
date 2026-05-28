#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, string> phonebook;
    phonebook["Alice"] = "415-555-0101";
    phonebook["Bob"] = "415-555-0202";
    phonebook["Charlie"] = "415-555-0303";

    string name = "Alice";
    if (phonebook.count(name)) {
        cout << name << "'s number: " << phonebook[name] << endl;
    } else {
        cout << name << " not found." << endl;
    }

    cout << "\nFull Phonebook:" << endl;
    for (const auto& [key, value] : phonebook) {
        cout << "  " << key << ": " << value << endl;
    }

    phonebook.erase("Bob");
    cout << "\nAfter deleting Bob:" << endl;
    for (const auto& [key, value] : phonebook) {
        cout << "  " << key << ": " << value << endl;
    }
    return 0;
}
