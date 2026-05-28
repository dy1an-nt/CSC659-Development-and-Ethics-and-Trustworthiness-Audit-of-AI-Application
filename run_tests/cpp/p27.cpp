#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string inputFile = "input.txt";
    string outputFile = "output_reversed.txt";

    ifstream inFile(inputFile);
    if (!inFile.is_open()) {
        cerr << "Error: Cannot open input file '" << inputFile << "'" << endl;
        return 1;
    }
    vector<string> lines;
    string line;
    while (getline(inFile, line)) {
        lines.push_back(line);
    }
    inFile.close();

    reverse(lines.begin(), lines.end());

    ofstream outFile(outputFile);
    if (!outFile.is_open()) {
        cerr << "Error: Cannot create output file '" << outputFile << "'" << endl;
        return 1;
    }
    for (const string& l : lines) {
        outFile << l << "\n";
    }
    outFile.close();

    cout << "Done. Reversed content written to '" << outputFile << "'" << endl;
    return 0;
}
