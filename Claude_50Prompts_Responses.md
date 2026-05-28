# Claude Model Responses – GenAI Coding Audit
## CSC 659-859 Spring 2026 – Team 06
**Model Tested:** Claude (claude-sonnet-4-20250514)  
**Tester:** Dylan Teopaco  
**Date:** 2026-05-12

> Source: Extracted directly from the original chat-history PDF
> (`Claude_Prompts_and_Responses_DylanTeopaco.pdf`).

---

## PYTHON – EASY

---

### P01 | Python (Easy)
**Prompt:** Write a function to check if a string is a palindrome (e.g., "radar"), ignoring spaces and  capitalization.

**Response:**
```python
def is_palindrome(s: str) -> bool: 
    """ 
    Check if a string is a palindrome, ignoring spaces and capitalization. 
  
    Args: 
        s: The input string to check. 
    Returns: 
        True if the string is a palindrome, False otherwise. 
    """ 
    cleaned = s.replace(" ", "").lower() 
    return cleaned == cleaned[::-1] 
  
# Test cases 
print(is_palindrome("radar"))        # True 
print(is_palindrome("A man a plan a canal Panama"))  # True (after spaces removed) 
print(is_palindrome("hello"))        # False 
print(is_palindrome("Racecar"))      # True
```

---

### P02 | Python (Easy)
**Prompt:** Create a list of numbers from 1 to 10 and print only the even ones using a loop.

**Response:**
```python
numbers = list(range(1, 11)) 
  
for num in numbers: 
    if num % 2 == 0: 
        print(num)
```

---

### P03 | Python (Easy)
**Prompt:** Write a script to calculate the area of a circle given the radius as input.

**Response:**
```python
import math 
  
def circle_area(radius: float) -> float: 
    """Calculate the area of a circle given its radius.""" 
    if radius < 0: 
        raise ValueError("Radius cannot be negative.") 
    return math.pi * radius ** 2 
  
# Get input from user 
try: 
    radius = float(input("Enter the radius: ")) 
    area = circle_area(radius) 
    print(f"The area of the circle with radius {radius} is: {area:.4f}") 
except ValueError as e: 
    print(f"Invalid input: {e}")
```

---

### P04 | Python (Easy)
**Prompt:** Reverse a list of integers without using the built-in .reverse() method.

**Response:**
```python
def reverse_list(lst: list) -> list: 
    """Reverse a list of integers without using .reverse().""" 
    reversed_lst = [] 
    for i in range(len(lst) - 1, -1, -1): 
        reversed_lst.append(lst[i]) 
    return reversed_lst 
  
# Test 
original = [1, 2, 3, 4, 5] 
print("Original:", original) 
print("Reversed:", reverse_list(original))
```

---

### P05 | Python (Easy)
**Prompt:** Create a dictionary of 3 fruits and their prices, then print the price of 'Apple'.

**Response:**
```python
fruit_prices = { 
    "Apple": 1.50, 
    "Banana": 0.75, 
    "Cherry": 3.00 
} 
  
print(f"The price of Apple is: ${fruit_prices['Apple']:.2f}")
```

---

### P06 | Python (Easy)
**Prompt:** Write a function that converts Celsius to Fahrenheit.

**Response:**
```python
def celsius_to_fahrenheit(celsius: float) -> float: 
    """ 
    Convert a temperature from Celsius to Fahrenheit. 
    Formula: F = (C x 9/5) + 32 
    """ 
    return (celsius * 9 / 5) + 32 
  
# Test cases 
test_values = [0, 100, -40, 37] 
for c in test_values: 
    f = celsius_to_fahrenheit(c) 
    print(f"{c}C = {f:.2f}F")
```

---

## C++ – EASY

---

### P07 | C++ (Easy)
**Prompt:** Write a program to find the largest of three numbers using if-else statements.

**Response:**
```cpp
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
```

---

### P08 | C++ (Easy)
**Prompt:** Demonstrate how to declare and initialize a 1D array of 5 integers and print them using a  range-based for loop.

**Response:**
```cpp
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
```

---

### P09 | C++ (Easy)
**Prompt:** Create a Rectangle class with private members width and height and a public function to  calculate the area.

**Response:**
```cpp
#include <iostream> 
using namespace std; 
  
class Rectangle { 
private: 
    double width; 
    double height; 
  
public: 
    Rectangle(double w, double h) : width(w), height(h) {} 
  
    double calculateArea() const { 
        return width * height; 
    } 
  
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
```

---

### P10 | C++ (Easy)
**Prompt:** Use a for loop to print the first 10 numbers of the Fibonacci sequence in C++.

**Response:**
```cpp
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
```

---

### P11 | C++ (Easy)
**Prompt:** Write a function that swaps two integers using references and explain why references are  used here.

**Response:**
```cpp
#include <iostream> 
using namespace std; 
  
void swapIntegers(int& a, int& b) { 
    int temp = a; 
    a = b; 
    b = temp; 
} 
  
int main() { 
    int x = 5, y = 10; 
    cout << "Before swap: x = " << x << ", y = " << y << endl; 
    swapIntegers(x, y); 
    cout << "After swap:  x = " << x << ", y = " << y << endl; 
    return 0; 
}
```

---

## JAVA – EASY

---

### P12 | Java (Easy)
**Prompt:** Write a simple Main class that prints "Hello, World!" and the current system date/time.

**Response:**
```java
import java.time.LocalDateTime; 
import java.time.format.DateTimeFormatter; 
  
public class Main { 
    public static void main(String[] args) { 
        System.out.println("Hello, World!"); 
  
        LocalDateTime now = LocalDateTime.now(); 
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"); 
        System.out.println("Current date/time: " + now.format(formatter)); 
    } 
}
```

---

### P13 | Java (Easy)
**Prompt:** Create an ArrayList of strings, add 3 names to it, and print them using a forEach loop.

**Response:**
```java
import java.util.ArrayList; 
  
public class Main { 
    public static void main(String[] args) { 
        ArrayList<String> names = new ArrayList<>(); 
        names.add("Alice"); 
        names.add("Bob"); 
        names.add("Charlie"); 
  
        System.out.println("Names in the list:"); 
        names.forEach(name -> System.out.println("  " + name)); 
    } 
}
```

---

### P14 | Java (Easy)
**Prompt:** Write a method called isPrime that takes an integer and returns true if it is prime, and false  otherwise.

**Response:**
```java
public class Main { 
    public static boolean isPrime(int n) { 
        if (n < 2) return false; 
        if (n == 2) return true; 
        if (n % 2 == 0) return false; 
        for (int i = 3; i <= Math.sqrt(n); i += 2) { 
            if (n % i == 0) return false; 
        } 
        return true; 
    } 
  
    public static void main(String[] args) { 
        int[] testValues = {1, 2, 3, 4, 17, 18, 97}; 
        for (int n : testValues) { 
            System.out.println(n + " is prime: " + isPrime(n)); 
        } 
    } 
}
```

---

### P15 | Java (Easy)
**Prompt:** Demonstrate the use of try-catch blocks to handle a potential NullPointerException.

**Response:**
```java
public class Main { 
    public static void main(String[] args) { 
        String text = null; 
  
        try { 
            // This will throw NullPointerException because text is null 
            int length = text.length(); 
            System.out.println("Length: " + length); 
        } catch (NullPointerException e) { 
            System.out.println("Caught NullPointerException: The string is null."); 
            System.out.println("Details: " + e.getMessage()); 
        } finally { 
            System.out.println("Finally block always executes."); 
        } 
  
        // Safe alternative using a null check 
        String safeText = (text != null) ? text : "default"; 
        System.out.println("Safe value: " + safeText); 
    } 
}
```

---

### P16 | Java (Easy)
**Prompt:** Create a simple Car class with a constructor (model, year) and a displayInfo() method.

**Response:**
```java
public class Car { 
    private String model; 
    private int year; 
  
    public Car(String model, int year) { 
        this.model = model; 
        this.year = year; 
    } 
  
    public void displayInfo() { 
        System.out.println("Car Model: " + model + " | Year: " + year); 
    } 
  
    public static void main(String[] args) { 
        Car car1 = new Car("Toyota Camry", 2022); 
        Car car2 = new Car("Ford Mustang", 1969); 
  
        car1.displayInfo(); 
        car2.displayInfo(); 
    } 
}
```

---

## PYTHON – MEDIUM

---

### P17 | Python (Medium)
**Prompt:** Implement a Binary Search algorithm on a sorted list of integers and explain its time  complexity.

**Response:**
```python
def binary_search(arr: list, target: int) -> int: 
    """ 
    Search for target in a sorted list using binary search. 
    Returns the index if found, -1 otherwise. 
    Time complexity: O(log n) 
    """ 
    left, right = 0, len(arr) - 1 
  
    while left <= right: 
        mid = left + (right - left) // 2  # Avoids integer overflow 
  
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target: 
            left = mid + 1  # Target is in the right half 
        else: 
            right = mid - 1  # Target is in the left half 
  
    return -1  # Target not found 
  
# Test 
sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91] 
print(binary_search(sorted_list, 23))   # Output: 5 
print(binary_search(sorted_list, 100))  # Output: -1
```

---

### P18 | Python (Medium)
**Prompt:** Write a script to read a local CSV file and calculate the average of a column named "Price".

**Response:**
```python
import csv 
  
def calculate_average_price(filepath: str) -> float: 
    """ 
    Read a CSV file and calculate the average value of the 'Price' column. 
    """ 
    prices = [] 
    try: 
        with open(filepath, newline='', encoding='utf-8') as csvfile: 
            reader = csv.DictReader(csvfile) 
            if 'Price' not in reader.fieldnames: 
                raise ValueError("CSV file does not contain a 'Price' column.") 
            for row in reader: 
                try: 
                    prices.append(float(row['Price'])) 
                except ValueError: 
                    print(f"Skipping non-numeric value: {row['Price']}") 
        if not prices: 
            raise ValueError("No valid price data found.") 
        return sum(prices) / len(prices) 
    except FileNotFoundError: 
        print(f"Error: File '{filepath}' not found.") 
        return 0.0 
  
# Demo with in-memory CSV 
import io 
sample_csv = """Name,Price,Category 
Apple,1.50,Fruit 
Banana,0.75,Fruit 
Cherry,3.00,Fruit 
Mango,2.25,Fruit 
""" 
reader = csv.DictReader(io.StringIO(sample_csv)) 
prices = [float(row['Price']) for row in reader] 
avg = sum(prices) / len(prices) 
print(f"Average Price: ${avg:.2f}")  # Output: $1.88
```

---

### P19 | Python (Medium)
**Prompt:** Create a function that takes a paragraph of text and returns a dictionary with the frequency  of each word.

**Response:**
```python
import re 
from collections import Counter 
  
def word_frequency(text: str) -> dict: 
    """ 
    Count the frequency of each word in a paragraph. 
    Ignores punctuation and is case-insensitive. 
    Returns a dictionary sorted by frequency (descending). 
    """ 
    words = re.findall(r'\b[a-z]+\b', text.lower()) 
    freq = Counter(words) 
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)) 
  
# Test 
paragraph = "The quick brown fox jumps over the lazy dog. The dog barked at the fox." 
result = word_frequency(paragraph) 
print(result)
```

---

### P20 | Python (Medium)
**Prompt:** Implement a simple Python Decorator that prints the execution time of any function it wraps.

**Response:**
```python
import time 
import functools 
  
def timer(func): 
    """Decorator that prints the execution time of any function.""" 
    @functools.wraps(func)  # Preserves original function metadata 
    def wrapper(*args, **kwargs): 
        start = time.perf_counter() 
        result = func(*args, **kwargs) 
        end = time.perf_counter() 
        elapsed = end - start 
        print(f"[TIMER] '{func.__name__}' executed in {elapsed:.6f} seconds") 
        return result 
    return wrapper 
  
@timer 
def slow_function(): 
    """Simulates a slow operation.""" 
    time.sleep(0.5) 
    return "done" 
  
@timer 
def sum_large(n): 
    return sum(range(n)) 
  
# Tests 
result1 = slow_function() 
result2 = sum_large(10_000_000) 
print(f"Sum result: {result2}")
```

---

### P21 | Python (Medium)
**Prompt:** Solve the "Two Sum" problem: Given an array of integers, return indices of the two numbers  such that they add up to a specific target.

**Response:**
```python
def two_sum(nums: list, target: int) -> list: 
    """ 
    Find indices of two numbers that add up to the target. 
    Uses a hash map for O(n) time complexity. 
    Returns [] if no solution exists. 
    """ 
    seen = {}  # Maps value -> index 
    for i, num in enumerate(nums): 
        complement = target - num 
        if complement in seen: 
            return [seen[complement], i] 
        seen[num] = i 
    return []  # No solution found 
  
# Test cases 
print(two_sum([2, 7, 11, 15], 9))   # [0, 1] 
print(two_sum([3, 2, 4], 6))        # [1, 2] 
print(two_sum([3, 3], 6))           # [0, 1] 
print(two_sum([1, 2, 3], 10))       # []
```

---

### P22 | Python (Medium)
**Prompt:** Write a script to find the longest common prefix string amongst an array of strings.

**Response:**
```python
def longest_common_prefix(strs: list) -> str: 
    """ 
    Find the longest common prefix among a list of strings. 
    Time complexity: O(S) where S is the sum of all characters. 
    """ 
    if not strs: 
        return "" 
    prefix = strs[0] 
    for s in strs[1:]: 
        while not s.startswith(prefix): 
            prefix = prefix[:-1] 
            if not prefix: 
                return "" 
    return prefix 
  
# Test cases 
print(longest_common_prefix(["flower", "flow", "flight"]))            # "fl" 
print(longest_common_prefix(["dog", "racecar", "car"]))               # "" 
print(longest_common_prefix(["interview", "interact", "interface"]))  # "inter" 
print(longest_common_prefix(["alone"]))                                # "alone"
```

---

## C++ – MEDIUM

---

### P23 | C++ (Medium)
**Prompt:** Implement a Singly Linked List with methods to insert a node at the head and display all  nodes.

**Response:**
```cpp
#include <iostream> 
using namespace std; 
  
struct Node { 
    int data; 
    Node* next; 
    Node(int val) : data(val), next(nullptr) {} 
}; 
  
class SinglyLinkedList { 
private: 
    Node* head; 
public: 
    SinglyLinkedList() : head(nullptr) {} 
  
    void insertAtHead(int val) { 
        Node* newNode = new Node(val); 
        newNode->next = head; 
        head = newNode; 
    } 
  
    void display() const { 
        Node* current = head; 
        cout << "List: "; 
        while (current != nullptr) { 
            cout << current->data; 
            if (current->next) cout << " -> "; 
            current = current->next; 
        } 
        cout << " -> NULL" << endl; 
    } 
  
    ~SinglyLinkedList() { 
        Node* current = head; 
        while (current != nullptr) { 
            Node* next = current->next; 
            delete current; 
            current = next; 
        } 
    } 
}; 
  
int main() { 
    SinglyLinkedList list; 
    list.insertAtHead(30); 
    list.insertAtHead(20); 
    list.insertAtHead(10); 
    list.display(); 
    return 0; 
}
```

---

### P24 | C++ (Medium)
**Prompt:** Explain and demonstrate the difference between a Shallow Copy and a Deep Copy using a  class with a pointer member.

**Response:**
```cpp
#include <iostream> 
#include <cstring> 
using namespace std; 
  
class MyString { 
public: 
    char* data; 
  
    MyString(const char* str) { 
        data = new char[strlen(str) + 1]; 
        strcpy(data, str); 
    } 
  
    // --- DEEP COPY (correct implementation) --- 
    MyString(const MyString& other) { 
        data = new char[strlen(other.data) + 1]; 
        strcpy(data, other.data); 
        cout << "[Deep Copy constructor called]" << endl; 
    } 
  
    void display() const { 
        cout << "Data: " << data << " (address: " << (void*)data << ")" << endl; 
    } 
  
    ~MyString() { 
        delete[] data; 
    } 
}; 
  
int main() { 
    MyString original("Hello"); 
    MyString copy(original);  // Deep copy 
  
    cout << "Original: "; original.display(); 
    cout << "Copy:     "; copy.display(); 
  
    strcpy(copy.data, "World"); 
    cout << "\nAfter modifying copy:" << endl; 
    cout << "Original: "; original.display(); 
    cout << "Copy:     "; copy.display(); 
  
    return 0; 
}
```

---

### P25 | C++ (Medium)
**Prompt:** Use std::sort with a custom lambda function to sort a std::vector of Person objects by their  age field.

**Response:**
```cpp
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
```

---

### P26 | C++ (Medium)
**Prompt:** Write a recursive function to solve the "Tower of Hanoi" problem for n disks and print the  moves.

**Response:**
```cpp
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
```

---

### P27 | C++ (Medium)
**Prompt:** Write a program that reads from one text file and writes its content into another file in  reverse order.

**Response:**
```cpp
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
```

---

### P28 | C++ (Medium)
**Prompt:** Demonstrate the use of std::map to store and retrieve phonebook entries (Name as key,  Number as value).

**Response:**
```cpp
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
```

---

## JAVA – MEDIUM

---

### P29 | Java (Medium)
**Prompt:** Implement a Stack data structure using an array with push, pop, and isEmpty methods.

**Response:**
```java
public class ArrayStack { 
    private int[] stack; 
    private int top; 
    private int capacity; 
  
    public ArrayStack(int capacity) { 
        this.capacity = capacity; 
        this.stack = new int[capacity]; 
        this.top = -1; 
    } 
  
    public void push(int value) { 
        if (top == capacity - 1) { 
            throw new RuntimeException("Stack overflow: stack is full."); 
        } 
        stack[++top] = value; 
        System.out.println("Pushed: " + value); 
    } 
  
    public int pop() { 
        if (isEmpty()) { 
            throw new RuntimeException("Stack underflow: stack is empty."); 
        } 
        return stack[top--]; 
    } 
  
    public int peek() { 
        if (isEmpty()) throw new RuntimeException("Stack is empty."); 
        return stack[top]; 
    } 
  
    public boolean isEmpty() { 
        return top == -1; 
    } 
  
    public static void main(String[] args) { 
        ArrayStack stack = new ArrayStack(5); 
        stack.push(10); 
        stack.push(20); 
        stack.push(30); 
        System.out.println("Peek: " + stack.peek()); 
        System.out.println("Popped: " + stack.pop()); 
        System.out.println("Popped: " + stack.pop()); 
        System.out.println("Is empty: " + stack.isEmpty()); 
    } 
}
```

---

### P30 | Java (Medium)
**Prompt:** Demonstrate method overriding with an abstract Shape class and concrete Circle and  Rectangle subclasses.

**Response:**
```java
public class ShapeDemo { 
  
    abstract static class Shape { 
        public abstract double calculateArea(); 
  
        public String describe() { 
            return "I am a Shape with area: " + calculateArea(); 
        } 
    } 
  
    static class Circle extends Shape { 
        private double radius; 
  
        public Circle(double radius) { 
            this.radius = radius; 
        } 
  
        @Override 
        public double calculateArea() { 
            return Math.PI * radius * radius; 
        } 
  
        @Override 
        public String toString() { 
            return String.format("Circle (radius=%.2f) -> Area: %.4f", radius, calculateArea()); 
        } 
    } 
  
    static class Rectangle extends Shape { 
        private double width, height; 
  
        public Rectangle(double width, double height) { 
            this.width = width; 
            this.height = height; 
        } 
  
        @Override 
        public double calculateArea() { 
            return width * height; 
        } 
    } 
  
    public static void main(String[] args) { 
        Shape[] shapes = { new Circle(5.0), new Rectangle(4.0, 6.0) }; 
  
        for (Shape s : shapes) { 
            System.out.println(s.describe()); 
        } 
  
        Circle c = new Circle(3.0);
System.out.println(c); 
    } 
}
```

---

### P31 | Java (Medium)
**Prompt:** Write a program to find the intersection of two integer arrays and return the common  elements in a new array.

**Response:**
```java
import java.util.*; 
  
public class ArrayIntersection { 
    public static int[] intersection(int[] arr1, int[] arr2) { 
        Set<Integer> set1 = new HashSet<>(); 
        Set<Integer> resultSet = new HashSet<>(); 
  
        for (int num : arr1) set1.add(num); 
        for (int num : arr2) { 
            if (set1.contains(num)) resultSet.add(num); 
        } 
  
        return resultSet.stream().mapToInt(Integer::intValue).toArray(); 
    } 
  
    public static void main(String[] args) { 
        int[] a = {1, 2, 3, 4, 5}; 
        int[] b = {3, 4, 5, 6, 7}; 
        int[] result = intersection(a, b); 
  
        System.out.println("Intersection: " + Arrays.toString(result)); 
    } 
}
```

---

### P32 | Java (Medium)
**Prompt:** Use an Interface to define a Playable behavior with a method play(). Implement this  interface in classes Guitar and Piano.

**Response:**
```java
public class InstrumentDemo { 
  
    interface Playable { 
        void play(); 
        default String getType() { 
            return "Unknown Instrument"; 
        } 
    } 
  
    static class Guitar implements Playable { 
        private String brand; 
  
        public Guitar(String brand) { 
            this.brand = brand; 
        } 
  
        @Override 
        public void play() { 
            System.out.println(brand + " Guitar: Strumming chords..."); 
        } 
  
        @Override 
        public String getType() { 
            return "String Instrument"; 
        } 
    } 
  
    static class Piano implements Playable { 
        @Override 
        public void play() { 
            System.out.println("Piano: Playing a melody..."); 
        } 
    } 
  
    public static void main(String[] args) { 
        Playable[] instruments = { new Guitar("Fender"), new Piano() }; 
  
        for (Playable instrument : instruments) { 
            instrument.play(); 
            System.out.println("  Type: " + instrument.getType()); 
        } 
    } 
}
```

---

### P33 | Java (Medium)
**Prompt:** Write a function to check if two strings are Anagrams of each other (e.g., "listen" and  "silent").

**Response:**
```java
import java.util.Arrays; 
  
public class AnagramCheck { 
    public static boolean isAnagram(String s1, String s2) { 
        if (s1 == null || s2 == null) return false; 
        s1 = s1.replaceAll("\\s+", "").toLowerCase(); 
        s2 = s2.replaceAll("\\s+", "").toLowerCase(); 
  
        if (s1.length() != s2.length()) return false; 
  
        char[] c1 = s1.toCharArray(); 
        char[] c2 = s2.toCharArray(); 
        Arrays.sort(c1); 
        Arrays.sort(c2); 
  
        return Arrays.equals(c1, c2); 
    } 
  
    public static void main(String[] args) { 
        System.out.println(isAnagram("listen", "silent"));          // true 
        System.out.println(isAnagram("Astronomer", "Moon starer")); // true 
        System.out.println(isAnagram("hello", "world"));            // false 
        System.out.println(isAnagram("Dormitory", "Dirty room"));   // true 
    } 
}
```

---

## PYTHON – HARD

---

### P34 | Python (Hard)
**Prompt:** Write a multithreaded Python script that simulates downloading 5 mock image URLs  concurrently and prints when each is finished.

**Response:**
```python
import threading 
import time 
import random 
  
def mock_download(url: str, index: int) -> None: 
    """Simulate downloading a file from a URL.""" 
    delay = random.uniform(0.5, 2.5) 
    print(f"[Thread {index}] Starting download: {url}") 
    time.sleep(delay)  # Simulate network latency 
    print(f"[Thread {index}] Finished: {url} (took {delay:.2f}s)") 
  
def download_all(urls: list) -> None: 
    """Download all URLs concurrently using threads.""" 
    threads = [] 
    for i, url in enumerate(urls): 
        t = threading.Thread(target=mock_download, args=(url, i + 1)) 
        threads.append(t) 
        t.start() 
    for t in threads: 
        t.join() 
    print("\nAll downloads complete.") 
  
image_urls = [ 
    "https://example.com/image1.png", 
    "https://example.com/image2.jpg", 
    "https://example.com/image3.gif", 
    "https://example.com/image4.webp", 
    "https://example.com/image5.png", 
] 
  
start = time.perf_counter() 
download_all(image_urls) 
total = time.perf_counter() - start 
print(f"Total time: {total:.2f}s")
```

---

### P35 | Python (Hard)
**Prompt:** Implement a thread-safe Singleton design pattern in Python and explain why it is necessary  in certain applications.

**Response:**
```python
import threading 
  
class ThreadSafeSingleton: 
    """Thread-safe Singleton using double-checked locking.""" 
    _instance = None 
    _lock = threading.Lock() 
  
    def __new__(cls): 
        if cls._instance is None:           # First check (no lock needed) 
            with cls._lock:                 # Acquire lock only when needed 
                if cls._instance is None:   # Second check (with lock) 
                    cls._instance = super().__new__(cls) 
                    cls._instance._initialized = False 
        return cls._instance 
  
    def __init__(self): 
        if not self._initialized: 
            self._initialized = True 
            self.data = {} 
            print(f"Singleton initialized (id={id(self)})") 
  
    def set(self, key, value): 
        self.data[key] = value 
  
    def get(self, key): 
        return self.data.get(key) 
  
  
def create_singleton(results, index): 
    s = ThreadSafeSingleton() 
    results[index] = id(s) 
  
results = [None] * 5 
threads = [threading.Thread(target=create_singleton, args=(results, i)) for i in range(5)] 
[t.start() for t in threads] 
[t.join() for t in threads] 
  
print("All instance IDs:", results) 
print("All same?", len(set(results)) == 1)
```

---

### P36 | Python (Hard - Audit)
**Prompt:** Audit Task: Identify and fix the SQL injection vulnerability in this code: query = "SELECT *  FROM users WHERE id=" + user_id. Show the secure way to do this.

**Response:**
```python
import sqlite3 
  
# ========== VULNERABLE CODE (DO NOT USE) ========== 
def get_user_vulnerable(conn, user_id: str): 
    """ 
    VULNERABLE: String concatenation allows SQL injection. 
    """ 
    query = "SELECT * FROM users WHERE id=" + user_id  # DANGEROUS 
    cursor = conn.execute(query) 
    return cursor.fetchall() 
  
# ========== SECURE CODE ========== 
def get_user_secure(conn, user_id: int): 
    """ 
    SECURE: Uses parameterized queries (prepared statements). 
    """ 
    query = "SELECT * FROM users WHERE id = ?"   # Placeholder 
    cursor = conn.execute(query, (user_id,))     # Parameters passed separately 
    return cursor.fetchall() 
  
# Demo 
conn = sqlite3.connect(":memory:") 
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)") 
conn.execute("INSERT INTO users VALUES (1, 'Alice')") 
conn.execute("INSERT INTO users VALUES (2, 'Bob')") 
conn.commit() 
  
print("Safe query result:", get_user_secure(conn, 1)) 
  
malicious_input = "1 OR 1=1" 
result = get_user_secure(conn, malicious_input) 
print("Attempted injection result:", result) 
  
conn.close()
```

---

### P37 | Python (Hard)
**Prompt:** Refactor a deeply nested if-else function (at least 4 levels deep) into a cleaner version using  a dispatch table or dictionary mapping.

**Response:**
```python
# ===== BEFORE: Deeply Nested if-else (4+ levels) ===== 
def process_action_nested(user_type: str, action: str, target: str) -> str: 
    if user_type == "admin": 
        if action == "create": 
            if target == "user": 
                return "Admin created a user" 
            else: 
                return "Admin created a resource" 
        elif action == "delete": 
            if target == "user": 
                return "Admin deleted a user" 
            else: 
                return "Admin deleted a resource" 
        else: 
            return "Admin: unknown action" 
    elif user_type == "guest": 
        if action == "read": 
            if target == "post": 
                return "Guest read a post" 
            else: 
                return "Guest read a resource" 
        else: 
            return "Guest: action not permitted" 
    else: 
        return "Unknown user type" 
  
  
# ===== AFTER: Clean Dispatch Table ===== 
ACTION_MAP = { 
    ("admin", "create", "user"):     "Admin created a user", 
    ("admin", "create", "resource"): "Admin created a resource", 
    ("admin", "delete", "user"):     "Admin deleted a user", 
    ("admin", "delete", "resource"): "Admin deleted a resource", 
    ("guest", "read", "post"):       "Guest read a post", 
    ("guest", "read", "resource"):   "Guest read a resource", 
} 
  
def process_action_clean(user_type: str, action: str, target: str) -> str: 
    """Use a dispatch table (dict) to map (user, action, target) -> result.""" 
    key = (user_type, action, target) 
    if key in ACTION_MAP: 
        return ACTION_MAP[key] 
    if user_type == "guest" and action != "read": 
        return "Guest: action not permitted" 
    if user_type not in ("admin", "guest"): 
        return "Unknown user type" 
    return f"{user_type}: unknown action/target combination" 
  
  
test_cases = [ 
    ("admin", "create", "user"), 
    ("admin", "delete", "resource"),
("guest", "read", "post"), 
    ("guest", "delete", "post"), 
    ("hacker", "exploit", "db"), 
] 
  
print("Results:") 
for args in test_cases: 
    print(f"  {args} -> {process_action_clean(*args)}")
```

---

### P38 | Python (Hard)
**Prompt:** Write an efficient algorithm to find the longest palindromic substring in a given string and  analyze its complexity.

**Response:**
```python
def longest_palindromic_substring(s: str) -> str: 
    """ 
    Find the longest palindromic substring using Expand Around Center. 
    Time:  O(n^2) 
    Space: O(1) extra (excluding output) 
    """ 
    if not s: 
        return "" 
  
    start, max_len = 0, 1 
  
    def expand(left: int, right: int) -> int: 
        """Expand outward while characters match; return length.""" 
        while left >= 0 and right < len(s) and s[left] == s[right]: 
            left -= 1 
            right += 1 
        return right - left - 1 
  
    for i in range(len(s)): 
        odd_len = expand(i, i) 
        even_len = expand(i, i + 1) 
        best = max(odd_len, even_len) 
        if best > max_len: 
            max_len = best 
            start = i - (best - 1) // 2 
  
    return s[start : start + max_len] 
  
  
print(longest_palindromic_substring("babad"))         # "bab" or "aba" 
print(longest_palindromic_substring("cbbd"))          # "bb" 
print(longest_palindromic_substring("racecar"))       # "racecar" 
print(longest_palindromic_substring("abacdfgdcaba"))  # "aba" 
print(longest_palindromic_substring("a"))             # "a"
```

---

### P39 | Python (Hard)
**Prompt:** Create a custom Exception class InsufficientFundsError and demonstrate how to raise and  catch it in a simple banking simulation.

**Response:**
```python
class InsufficientFundsError(Exception): 
    """Raised when a withdrawal exceeds the available account balance.""" 
  
    def __init__(self, balance: float, amount: float): 
        self.balance = balance 
        self.amount = amount 
        self.deficit = amount - balance 
        super().__init__( 
            f"Insufficient funds: tried to withdraw ${amount:.2f}, " 
            f"but balance is only ${balance:.2f} (deficit: ${self.deficit:.2f})" 
        ) 
  
  
class BankAccount: 
    def __init__(self, owner: str, initial_balance: float = 0.0): 
        self.owner = owner 
        self._balance = initial_balance 
  
    def deposit(self, amount: float) -> None: 
        if amount <= 0: 
            raise ValueError("Deposit amount must be positive.") 
        self._balance += amount 
        print(f"Deposited ${amount:.2f} | New balance: ${self._balance:.2f}") 
  
    def withdraw(self, amount: float) -> None: 
        if amount <= 0: 
            raise ValueError("Withdrawal amount must be positive.") 
        if amount > self._balance: 
            raise InsufficientFundsError(self._balance, amount) 
        self._balance -= amount 
        print(f"Withdrew ${amount:.2f} | New balance: ${self._balance:.2f}") 
  
    @property 
    def balance(self) -> float: 
        return self._balance 
  
  
account = BankAccount("Alice", initial_balance=500.00) 
  
try: 
    account.deposit(200.00) 
    account.withdraw(300.00) 
    account.withdraw(600.00)  # Should raise InsufficientFundsError 
except InsufficientFundsError as e: 
    print(f"\nError caught: {e}") 
    print(f"  Account balance: ${e.balance:.2f}") 
    print(f"  You are short: ${e.deficit:.2f}")
```

---

## C++ – HARD

---

### P40 | C++ (Hard - Audit)
**Prompt:** Memory Management Audit: Detect and fix the memory leak in: void func() { int* arr = new  int[100]; if (true) return; delete[] arr; }

**Response:**
```cpp
#include <iostream> 
#include <memory> 
#include <vector> 
  
// ===== VULNERABLE (memory leak) ===== 
void func_leaky() { 
    int* arr = new int[100]; 
    if (true) return;    // Always returns here — delete[] NEVER reached! 
    delete[] arr;        // Dead code 
} 
  
// ===== FIX 1: Ensure delete is always called ===== 
void func_fixed_manual() { 
    int* arr = new int[100]; 
    // ... use arr ... 
    delete[] arr;        // Must always be reached — fragile in complex code 
    return; 
} 
  
// ===== FIX 2 (Recommended): Use std::unique_ptr — RAII ===== 
void func_fixed_raii() { 
    std::unique_ptr<int[]> arr = std::make_unique<int[]>(100); 
    if (true) return;    // No leak! Destructor called automatically. 
} 
  
// ===== FIX 3: Use std::vector — simplest ===== 
void func_fixed_vector() { 
    std::vector<int> arr(100); 
    if (true) return;    // Automatically freed when it goes out of scope 
} 
  
int main() { 
    func_leaky();        // Leaks 100 * sizeof(int) = ~400 bytes 
    func_fixed_raii();   // Safe 
    func_fixed_vector(); // Safe 
    std::cout << "No leaks (in fixed versions)" << std::endl; 
    return 0; 
}
```

---

### P41 | C++ (Hard)
**Prompt:** Refactor a program that uses raw pointers for resource management to use std::unique_ptr  and std::shared_ptr to ensure exception safety.

**Response:**
```cpp
#include <iostream> 
#include <memory> 
#include <vector> 
using namespace std; 
  
// ===== BEFORE: Raw pointers (exception-unsafe) ===== 
class ResourceRaw { 
    int* data; 
public: 
    ResourceRaw(int size) : data(new int[size]) { 
        cout << "Raw resource acquired" << endl; 
    } 
    ~ResourceRaw() { delete[] data; cout << "Raw resource freed" << endl; } 
}; 
  
// ===== AFTER: unique_ptr (sole ownership) ===== 
class ResourceUnique { 
    unique_ptr<int[]> data; 
public: 
    ResourceUnique(int size) : data(make_unique<int[]>(size)) { 
        cout << "Unique resource acquired" << endl; 
    } 
}; 
  
// ===== shared_ptr (shared ownership) ===== 
class SharedConfig { 
public: 
    string name; 
    SharedConfig(const string& n) : name(n) { 
        cout << "Config '" << name << "' created" << endl; 
    } 
    ~SharedConfig() { 
        cout << "Config '" << name << "' destroyed (ref count reached 0)" << endl; 
    } 
}; 
  
int main() { 
    { 
        auto res = make_unique<ResourceUnique>(100); 
    } 
    cout << "After unique scope" << endl; 
  
    shared_ptr<SharedConfig> config1 = make_shared<SharedConfig>("AppConfig"); 
    { 
        shared_ptr<SharedConfig> config2 = config1;  // ref count = 2 
        cout << "Inside scope, ref count: " << config1.use_count() << endl; 
    } 
    cout << "Outside scope, ref count: " << config1.use_count() << endl; 
  
    return 0; 
}
```

---

### P42 | C++ (Hard)
**Prompt:** Simulate a basic producer-consumer problem using std::mutex and std::condition_variable  to handle thread synchronization.

**Response:**
```cpp
#include <iostream> 
#include <thread> 
#include <queue> 
#include <mutex> 
#include <condition_variable> 
#include <chrono> 
using namespace std; 
  
queue<int> buffer; 
mutex mtx; 
condition_variable cv; 
const int MAX_BUFFER = 5; 
bool done = false; 
  
void producer(int n) { 
    for (int i = 1; i <= n; i++) { 
        unique_lock<mutex> lock(mtx); 
        cv.wait(lock, [] { return buffer.size() < MAX_BUFFER; }); 
  
        buffer.push(i); 
        cout << "[Producer] Produced: " << i << " (buffer size: " << buffer.size() << ")" << 
endl; 
  
        lock.unlock(); 
        cv.notify_all(); 
        this_thread::sleep_for(chrono::milliseconds(100)); 
    } 
    { 
        unique_lock<mutex> lock(mtx); 
        done = true; 
    } 
    cv.notify_all(); 
} 
  
void consumer(int id) { 
    while (true) { 
        unique_lock<mutex> lock(mtx); 
        cv.wait(lock, [] { return !buffer.empty() || done; }); 
  
        if (buffer.empty() && done) break; 
  
        int item = buffer.front(); 
        buffer.pop(); 
        cout << "[Consumer " << id << "] Consumed: " << item 
             << " (buffer size: " << buffer.size() << ")" << endl; 
  
        lock.unlock(); 
        cv.notify_all(); 
        this_thread::sleep_for(chrono::milliseconds(150)); 
    } 
}
int main() { 
    thread prod(producer, 10); 
    thread cons1(consumer, 1); 
    thread cons2(consumer, 2); 
  
    prod.join(); 
    cons1.join(); 
    cons2.join(); 
  
    cout << "All done." << endl; 
    return 0; 
}
```

---

### P43 | C++ (Hard - Audit)
**Prompt:** Audit Task: Explain why the following code causes a Segmentation Fault and provide a  secure fix: int* p = nullptr; if (true) { int x = 10; p = &x; } cout << *p;

**Response:**
```cpp
#include <iostream> 
#include <memory> 
using namespace std; 
  
// ===== VULNERABLE: Dangling pointer / undefined behavior ===== 
void buggy() { 
    int* p = nullptr; 
    if (true) { 
        int x = 10; 
        p = &x; 
        // x lives on the stack — valid only within this block 
    } 
    // x is now OUT OF SCOPE. Its memory has been released. 
    // p is a "dangling pointer" — it points to deallocated stack memory. 
    cout << *p;  // UNDEFINED BEHAVIOR 
} 
  
// ===== FIX 1: Use heap allocation (caller manages lifetime) ===== 
void fix_heap() { 
    int* p = new int(10); 
    cout << "Value: " << *p << endl; 
    delete p; 
} 
  
// ===== FIX 2 (Recommended): Use local variable in correct scope ===== 
void fix_scope() { 
    int x = 10; 
    int* p = &x; 
    cout << "Value: " << *p << endl; 
} 
  
// ===== FIX 3: Use smart pointer ===== 
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
```

---

### P44 | C++ (Hard)
**Prompt:** Implement a custom String class that manages its own memory and adheres to the Rule of  Three (Destructor, Copy Constructor, Copy Assignment Operator).

**Response:**
```cpp
#include <iostream> 
#include <cstring> 
using namespace std; 
  
class MyString { 
private: 
    char* data; 
    size_t length; 
  
public: 
    // Constructor 
    MyString(const char* str = "") { 
        length = strlen(str); 
        data = new char[length + 1]; 
        strcpy(data, str); 
        cout << "[Constructor] \"" << data << "\"" << endl; 
    } 
  
    // 1. Destructor 
    ~MyString() { 
        cout << "[Destructor] \"" << data << "\"" << endl; 
        delete[] data; 
    } 
  
    // 2. Copy Constructor (deep copy) 
    MyString(const MyString& other) { 
        length = other.length; 
        data = new char[length + 1]; 
        strcpy(data, other.data); 
        cout << "[Copy Constructor] \"" << data << "\"" << endl; 
    } 
  
    // 3. Copy Assignment Operator (deep copy + self-assignment check) 
    MyString& operator=(const MyString& other) { 
        if (this == &other) return *this;  // Self-assignment guard 
        delete[] data; 
        length = other.length; 
        data = new char[length + 1]; 
        strcpy(data, other.data); 
        cout << "[Copy Assignment] \"" << data << "\"" << endl; 
        return *this; 
    } 
  
    const char* c_str() const { return data; } 
    size_t size() const { return length; } 
}; 
  
int main() { 
    MyString s1("Hello"); 
    MyString s2 = s1;     // Copy constructor 
    MyString s3("World");
s3 = s1;              // Copy assignment 
  
    cout << "\nValues: " << s1.c_str() << ", " << s2.c_str() << ", " << s3.c_str() << endl; 
    return 0; 
}
```

---

## JAVA – HARD

---

### P45 | Java (Hard)
**Prompt:** Create a thread-safe Singleton pattern using Double-Checked Locking and explain why the  volatile keyword is necessary.

**Response:**
```java
public class DatabaseConnection { 
    private volatile static DatabaseConnection instance; 
    private String connectionString; 
  
    private DatabaseConnection() { 
        this.connectionString = "jdbc:mysql://localhost:3306/mydb"; 
        System.out.println("DatabaseConnection created (id: " + System.identityHashCode(this) + 
")"); 
    } 
  
    public static DatabaseConnection getInstance() { 
        if (instance == null) {                     // First check (no lock) 
            synchronized (DatabaseConnection.class) { 
                if (instance == null) {             // Second check (with lock) 
                    instance = new DatabaseConnection(); 
                } 
            } 
        } 
        return instance; 
    } 
  
    public String getConnectionString() { 
        return connectionString; 
    } 
  
    public static void main(String[] args) throws InterruptedException { 
        Runnable task = () -> { 
            DatabaseConnection db = DatabaseConnection.getInstance(); 
            System.out.println(Thread.currentThread().getName() 
                + " got instance id: " + System.identityHashCode(db)); 
        }; 
  
        Thread[] threads = new Thread[5]; 
        for (int i = 0; i < 5; i++) { 
            threads[i] = new Thread(task, "Thread-" + i); 
            threads[i].start(); 
        } 
        for (Thread t : threads) t.join(); 
    } 
}
```

---

### P46 | Java (Hard - Audit)
**Prompt:** Audit Task: Analyze a snippet of multithreaded Java code, identify a potential Deadlock  scenario, and refactor it to be deadlock-free.

**Response:**
```java
public class DeadlockDemo { 
  
    static final Object LOCK_A = new Object(); 
    static final Object LOCK_B = new Object(); 
  
    // ===== DEADLOCK SCENARIO (shown for analysis, not run) ===== 
    static class Thread1 implements Runnable { 
        public void run() { 
            synchronized (LOCK_A) { 
                System.out.println("Thread1: holding LOCK_A, waiting for LOCK_B"); 
                try { Thread.sleep(50); } catch (InterruptedException e) {} 
                synchronized (LOCK_B) { 
                    System.out.println("Thread1: acquired both locks"); 
                } 
            } 
        } 
    } 
  
    static class Thread2 implements Runnable { 
        public void run() { 
            synchronized (LOCK_B) {  // opposite order — root cause 
                System.out.println("Thread2: holding LOCK_B, waiting for LOCK_A"); 
                try { Thread.sleep(50); } catch (InterruptedException e) {} 
                synchronized (LOCK_A) { 
                    System.out.println("Thread2: acquired both locks"); 
                } 
            } 
        } 
    } 
  
    // ===== DEADLOCK-FREE: Consistent Lock Ordering ===== 
    static class SafeThread1 implements Runnable { 
        public void run() { 
            synchronized (LOCK_A) {   // Always acquire A first 
                synchronized (LOCK_B) { 
                    System.out.println("SafeThread1: both locks acquired"); 
                } 
            } 
        } 
    } 
  
    static class SafeThread2 implements Runnable { 
        public void run() { 
            synchronized (LOCK_A) {   // Same order: A then B 
                synchronized (LOCK_B) { 
                    System.out.println("SafeThread2: both locks acquired"); 
                } 
            } 
        } 
    }
public static void main(String[] args) throws InterruptedException { 
        System.out.println("=== Safe version ==="); 
        Thread t1 = new Thread(new SafeThread1()); 
        Thread t2 = new Thread(new SafeThread2()); 
        t1.start(); t2.start(); 
        t1.join(); t2.join(); 
        System.out.println("Completed without deadlock."); 
    } 
}
```

---

### P47 | Java (Hard)
**Prompt:** Use the Java Stream API to take a list of Employee objects, filter those with salary > 50000,  group them by department, and calculate the average salary per department.

**Response:**
```java
import java.util.*; 
import java.util.stream.*; 
  
public class EmployeeAnalysis { 
  
    record Employee(String name, String department, double salary) {} 
  
    public static void main(String[] args) { 
        List<Employee> employees = List.of( 
            new Employee("Alice",   "Engineering", 95000), 
            new Employee("Bob",     "Engineering", 45000), 
            new Employee("Charlie", "Marketing",   62000), 
            new Employee("Diana",   "Engineering", 110000), 
            new Employee("Eve",     "Marketing",   48000), 
            new Employee("Frank",   "HR",          55000), 
            new Employee("Grace",   "HR",          40000) 
        ); 
  
        Map<String, Double> avgSalaryByDept = employees.stream() 
            .filter(e -> e.salary() > 50000) 
            .collect(Collectors.groupingBy( 
                Employee::department, 
                Collectors.averagingDouble(Employee::salary) 
            )); 
  
        System.out.println("Average salary by department (for employees earning > $50,000):"); 
        avgSalaryByDept.entrySet().stream() 
            .sorted(Map.Entry.comparingByKey()) 
            .forEach(entry -> 
                System.out.printf("  %-15s $%,.2f%n", entry.getKey(), entry.getValue())); 
    } 
}
```

---

### P48 | Java (Hard)
**Prompt:** Implement a Binary Search Tree (BST) and write a method to delete a node while  maintaining the BST properties.

**Response:**
```java
public class BST { 
    private static class Node { 
        int value; 
        Node left, right; 
        Node(int val) { this.value = val; } 
    } 
  
    private Node root; 
  
    public void insert(int val) { 
        root = insertRec(root, val); 
    } 
  
    private Node insertRec(Node node, int val) { 
        if (node == null) return new Node(val); 
        if (val < node.value) node.left = insertRec(node.left, val); 
        else if (val > node.value) node.right = insertRec(node.right, val); 
        return node; 
    } 
  
    public void delete(int val) { 
        root = deleteRec(root, val); 
    } 
  
    private Node deleteRec(Node node, int val) { 
        if (node == null) return null; 
  
        if (val < node.value) { 
            node.left = deleteRec(node.left, val); 
        } else if (val > node.value) { 
            node.right = deleteRec(node.right, val); 
        } else { 
            // Case 1: No children (leaf) 
            if (node.left == null && node.right == null) return null; 
            // Case 2: One child 
            if (node.left == null) return node.right; 
            if (node.right == null) return node.left; 
            // Case 3: Two children — inorder successor 
            Node successor = findMin(node.right); 
            node.value = successor.value; 
            node.right = deleteRec(node.right, successor.value); 
        } 
        return node; 
    } 
  
    private Node findMin(Node node) { 
        while (node.left != null) node = node.left; 
        return node; 
    } 
  
    public void inorder() {
inorderRec(root); 
        System.out.println(); 
    } 
  
    private void inorderRec(Node node) { 
        if (node == null) return; 
        inorderRec(node.left); 
        System.out.print(node.value + " "); 
        inorderRec(node.right); 
    } 
  
    public static void main(String[] args) { 
        BST tree = new BST(); 
        for (int v : new int[]{50, 30, 70, 20, 40, 60, 80}) tree.insert(v); 
  
        System.out.print("Initial (inorder): "); tree.inorder(); 
  
        tree.delete(20);  // Leaf node 
        System.out.print("After deleting 20: "); tree.inorder(); 
  
        tree.delete(30);  // One child 
        System.out.print("After deleting 30: "); tree.inorder(); 
  
        tree.delete(50);  // Two children (root) 
        System.out.print("After deleting 50: "); tree.inorder(); 
    } 
}
```

---

### P49 | Java (Hard)
**Prompt:** Refactoring Task: Take a large, monolithic method and refactor it into smaller, testable units  that adhere to the Single Responsibility Principle (SOLID).

**Response:**
```java
import java.util.*; 
  
public class OrderProcessor { 
  
    record Order(int id, List<Double> items, String customerEmail, String coupon) {} 
  
    // ===== BEFORE: Monolithic method (does everything) ===== 
    static void processOrderMonolithic(Order order) { 
        if (order.items() == null || order.items().isEmpty()) { 
            System.out.println("Error: empty order"); 
            return; 
        } 
        double total = 0; 
        for (double item : order.items()) total += item; 
        if ("SAVE10".equals(order.coupon())) total *= 0.90; 
        total *= 1.08; 
        System.out.println("Sending email to " + order.customerEmail() 
            + " | Total: $" + String.format("%.2f", total)); 
        System.out.println("Order #" + order.id() + " processed."); 
    } 
  
    // ===== AFTER: SRP-compliant, each class has one responsibility ===== 
  
    static class OrderValidator { 
        public boolean validate(Order order) { 
            return order.items() != null && !order.items().isEmpty(); 
        } 
    } 
  
    static class PriceCalculator { 
        public double calculateSubtotal(List<Double> items) { 
            return items.stream().mapToDouble(Double::doubleValue).sum(); 
        } 
        public double applyDiscount(double total, String coupon) { 
            if ("SAVE10".equals(coupon)) return total * 0.90; 
            return total; 
        } 
        public double applyTax(double subtotal, double taxRate) { 
            return subtotal * (1 + taxRate); 
        } 
    } 
  
    static class EmailService { 
        public void sendConfirmation(String email, double total) { 
            System.out.printf("Email sent to %s | Total: $%.2f%n", email, total); 
        } 
    } 
  
    static class OrderLogger { 
        public void log(int orderId) { 
            System.out.println("Order #" + orderId + " processed.");
} 
    } 
  
    static void processOrder(Order order) { 
        OrderValidator validator = new OrderValidator(); 
        PriceCalculator calculator = new PriceCalculator(); 
        EmailService emailService = new EmailService(); 
        OrderLogger logger = new OrderLogger(); 
  
        if (!validator.validate(order)) { 
            System.out.println("Error: invalid order"); return; 
        } 
        double subtotal = calculator.calculateSubtotal(order.items()); 
        subtotal = calculator.applyDiscount(subtotal, order.coupon()); 
        double total = calculator.applyTax(subtotal, 0.08); 
        emailService.sendConfirmation(order.customerEmail(), total); 
        logger.log(order.id()); 
    } 
  
    public static void main(String[] args) { 
        Order order = new Order(101, List.of(29.99, 49.99, 14.99), "alice@example.com", 
"SAVE10"); 
        processOrder(order); 
    } 
}
```

---

### P50 | Java (Hard)
**Prompt:** Implement Dijkstra's algorithm to find the shortest path in a weighted graph from a source  vertex to all other vertices.

**Response:**
```java
import java.util.*; 
  
public class Dijkstra { 
  
    static final int INF = Integer.MAX_VALUE; 
  
    public static int[] dijkstra(int[][] graph, int source) { 
        int n = graph.length; 
        int[] dist = new int[n]; 
        boolean[] visited = new boolean[n]; 
  
        Arrays.fill(dist, INF); 
        dist[source] = 0; 
  
        // Min-heap: [distance, vertex] 
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0])); 
        pq.offer(new int[]{0, source}); 
  
        while (!pq.isEmpty()) { 
            int[] curr = pq.poll(); 
            int u = curr[1]; 
  
            if (visited[u]) continue; 
            visited[u] = true; 
  
            for (int v = 0; v < n; v++) { 
                if (graph[u][v] != 0 && !visited[v]) { 
                    long newDist = (long) dist[u] + graph[u][v]; 
                    if (newDist < dist[v]) { 
                        dist[v] = (int) newDist; 
                        pq.offer(new int[]{dist[v], v}); 
                    } 
                } 
            } 
        } 
        return dist; 
    } 
  
    public static void main(String[] args) { 
        int[][] graph = { 
            {0, 4, 0, 0, 0, 0, 0, 8, 0}, 
            {4, 0, 8, 0, 0, 0, 0, 11, 0}, 
            {0, 8, 0, 7, 0, 4, 0, 0, 2}, 
            {0, 0, 7, 0, 9, 14, 0, 0, 0}, 
            {0, 0, 0, 9, 0, 10, 0, 0, 0}, 
            {0, 0, 4, 14, 10, 0, 2, 0, 0}, 
            {0, 0, 0, 0, 0, 2, 0, 1, 6}, 
            {8, 11, 0, 0, 0, 0, 1, 0, 7}, 
            {0, 0, 2, 0, 0, 0, 6, 7, 0} 
        };
int source = 0; 
        int[] distances = dijkstra(graph, source); 
  
        System.out.println("Shortest distances from vertex " + source + ":"); 
        for (int i = 0; i < distances.length; i++) { 
            System.out.printf("  To vertex %d: %d%n", i, distances[i]); 
        } 
    } 
}
```

---