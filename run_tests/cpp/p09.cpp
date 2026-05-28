#include <iostream>
using namespace std;

class Rectangle {
private:
    double width;
    double height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double calculateArea() const { return width * height; }
    void display() const {
        cout << "Rectangle " << width << " x " << height
             << " -> Area: " << calculateArea() << endl;
    }
};

int main() {
    Rectangle rect(5.0, 3.0);
    rect.display();
    cout << "Area: " << rect.calculateArea() << endl;
    return 0;
}
