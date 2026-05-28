#!/usr/bin/env python3
"""
Run all 50 coding prompts (Python, C++, Java), capture output, and save results.
"""
import subprocess
import os
import shutil
import time

BASE = os.path.dirname(os.path.abspath(__file__))

def run(cmd, cwd=None, stdin_text=None, timeout=30):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd,
            input=stdin_text, capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

results = []

# ─────────────────────────────────────────────
#  PYTHON PROMPTS
# ─────────────────────────────────────────────

# P01 – Palindrome check
p01 = """\
def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("radar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
print(is_palindrome("Racecar"))
"""
write_file(f"{BASE}/python/p01.py", p01)
rc, out, err = run("python3 p01.py", cwd=f"{BASE}/python")
results.append(("P01", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P02 – Even numbers
p02 = """\
numbers = list(range(1, 11))
for num in numbers:
    if num % 2 == 0:
        print(num)
"""
write_file(f"{BASE}/python/p02.py", p02)
rc, out, err = run("python3 p02.py", cwd=f"{BASE}/python")
results.append(("P02", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P03 – Circle area (uses input(); pipe a value)
p03 = """\
import math

def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

try:
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.4f}")
except ValueError as e:
    print(f"Invalid input: {e}")
"""
write_file(f"{BASE}/python/p03.py", p03)
rc, out, err = run("echo '5' | python3 p03.py", cwd=f"{BASE}/python")
results.append(("P03", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P04 – Reverse list
p04 = """\
def reverse_list(lst: list) -> list:
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

original = [1, 2, 3, 4, 5]
print("Original:", original)
print("Reversed:", reverse_list(original))
"""
write_file(f"{BASE}/python/p04.py", p04)
rc, out, err = run("python3 p04.py", cwd=f"{BASE}/python")
results.append(("P04", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P05 – Fruit prices dict
p05 = """\
fruit_prices = {
    "Apple": 1.50,
    "Banana": 0.75,
    "Cherry": 3.00
}
print(f"The price of Apple is: ${fruit_prices['Apple']:.2f}")
"""
write_file(f"{BASE}/python/p05.py", p05)
rc, out, err = run("python3 p05.py", cwd=f"{BASE}/python")
results.append(("P05", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P06 – Celsius to Fahrenheit
p06 = """\
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

test_values = [0, 100, -40, 37]
for c in test_values:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")
"""
write_file(f"{BASE}/python/p06.py", p06)
rc, out, err = run("python3 p06.py", cwd=f"{BASE}/python")
results.append(("P06", "Python", "Easy", rc == 0, out.strip(), err.strip()))

# P17 – Binary search
p17 = """\
def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
print(binary_search(sorted_list, 23))
print(binary_search(sorted_list, 100))
"""
write_file(f"{BASE}/python/p17.py", p17)
rc, out, err = run("python3 p17.py", cwd=f"{BASE}/python")
results.append(("P17", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P18 – CSV average price
p18 = """\
import csv
import io

sample_csv = \"\"\"Name,Price,Category
Apple,1.50,Fruit
Banana,0.75,Fruit
Cherry,3.00,Fruit
Mango,2.25,Fruit
\"\"\"

reader = csv.DictReader(io.StringIO(sample_csv))
prices = [float(row['Price']) for row in reader]
avg = sum(prices) / len(prices)
print(f"Average Price: ${avg:.2f}")
"""
write_file(f"{BASE}/python/p18.py", p18)
rc, out, err = run("python3 p18.py", cwd=f"{BASE}/python")
results.append(("P18", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P19 – Word frequency
p19 = """\
import re
from collections import Counter

def word_frequency(text: str) -> dict:
    words = re.findall(r'\\b[a-z]+\\b', text.lower())
    freq = Counter(words)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

paragraph = "The quick brown fox jumps over the lazy dog. The dog barked at the fox."
result = word_frequency(paragraph)
print(result)
"""
write_file(f"{BASE}/python/p19.py", p19)
rc, out, err = run("python3 p19.py", cwd=f"{BASE}/python")
results.append(("P19", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P20 – Timer decorator
p20 = """\
import time
import functools

def timer(func):
    @functools.wraps(func)
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
    time.sleep(0.1)
    return "done"

@timer
def sum_large(n):
    return sum(range(n))

result1 = slow_function()
result2 = sum_large(1_000_000)
print(f"Sum result: {result2}")
"""
write_file(f"{BASE}/python/p20.py", p20)
rc, out, err = run("python3 p20.py", cwd=f"{BASE}/python", timeout=15)
results.append(("P20", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P21 – Two sum
p21 = """\
def two_sum(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3], 10))
"""
write_file(f"{BASE}/python/p21.py", p21)
rc, out, err = run("python3 p21.py", cwd=f"{BASE}/python")
results.append(("P21", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P22 – Longest common prefix
p22 = """\
def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["interview", "interact", "interface"]))
print(longest_common_prefix(["alone"]))
"""
write_file(f"{BASE}/python/p22.py", p22)
rc, out, err = run("python3 p22.py", cwd=f"{BASE}/python")
results.append(("P22", "Python", "Medium", rc == 0, out.strip(), err.strip()))

# P34 – Multithreaded downloads (shortened sleep for speed)
p34 = """\
import threading
import time
import random

def mock_download(url: str, index: int) -> None:
    delay = random.uniform(0.05, 0.2)
    print(f"[Thread {index}] Starting download: {url}")
    time.sleep(delay)
    print(f"[Thread {index}] Finished: {url} (took {delay:.2f}s)")

def download_all(urls: list) -> None:
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=mock_download, args=(url, i + 1))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("\\nAll downloads complete.")

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
"""
write_file(f"{BASE}/python/p34.py", p34)
rc, out, err = run("python3 p34.py", cwd=f"{BASE}/python", timeout=15)
results.append(("P34", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# P35 – Thread-safe Singleton
p35 = """\
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
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
"""
write_file(f"{BASE}/python/p35.py", p35)
rc, out, err = run("python3 p35.py", cwd=f"{BASE}/python")
results.append(("P35", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# P36 – SQL injection audit
p36 = """\
import sqlite3

def get_user_secure(conn, user_id):
    query = "SELECT * FROM users WHERE id = ?"
    cursor = conn.execute(query, (user_id,))
    return cursor.fetchall()

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
"""
write_file(f"{BASE}/python/p36.py", p36)
rc, out, err = run("python3 p36.py", cwd=f"{BASE}/python")
results.append(("P36", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# P37 – Dispatch table refactor
p37 = """\
ACTION_MAP = {
    ("admin", "create", "user"):     "Admin created a user",
    ("admin", "create", "resource"): "Admin created a resource",
    ("admin", "delete", "user"):     "Admin deleted a user",
    ("admin", "delete", "resource"): "Admin deleted a resource",
    ("guest", "read", "post"):       "Guest read a post",
    ("guest", "read", "resource"):   "Guest read a resource",
}

def process_action_clean(user_type: str, action: str, target: str) -> str:
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
"""
write_file(f"{BASE}/python/p37.py", p37)
rc, out, err = run("python3 p37.py", cwd=f"{BASE}/python")
results.append(("P37", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# P38 – Longest palindromic substring
p38 = """\
def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    start, max_len = 0, 1

    def expand(left: int, right: int) -> int:
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

print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("racecar"))
print(longest_palindromic_substring("abacdfgdcaba"))
print(longest_palindromic_substring("a"))
"""
write_file(f"{BASE}/python/p38.py", p38)
rc, out, err = run("python3 p38.py", cwd=f"{BASE}/python")
results.append(("P38", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# P39 – Custom exception
p39 = """\
class InsufficientFundsError(Exception):
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
    account.withdraw(600.00)
except InsufficientFundsError as e:
    print(f"\\nError caught: {e}")
    print(f"  Account balance: ${e.balance:.2f}")
    print(f"  You are short: ${e.deficit:.2f}")
"""
write_file(f"{BASE}/python/p39.py", p39)
rc, out, err = run("python3 p39.py", cwd=f"{BASE}/python")
results.append(("P39", "Python", "Hard", rc == 0, out.strip(), err.strip()))

# ─────────────────────────────────────────────
#  C++ PROMPTS
# ─────────────────────────────────────────────

# P07 – Largest of three (uses cin; pipe input)
p07 = """\
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
"""
write_file(f"{BASE}/cpp/p07.cpp", p07)
rc, out, err = run("g++ -o p07 p07.cpp && echo '10 20 15' | ./p07", cwd=f"{BASE}/cpp")
results.append(("P07", "C++", "Easy", rc == 0, out.strip(), err.strip()))

# P08 – Array with range-based for
p08 = """\
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
"""
write_file(f"{BASE}/cpp/p08.cpp", p08)
rc, out, err = run("g++ -o p08 p08.cpp && ./p08", cwd=f"{BASE}/cpp")
results.append(("P08", "C++", "Easy", rc == 0, out.strip(), err.strip()))

# P09 – Rectangle class
p09 = """\
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
"""
write_file(f"{BASE}/cpp/p09.cpp", p09)
rc, out, err = run("g++ -o p09 p09.cpp && ./p09", cwd=f"{BASE}/cpp")
results.append(("P09", "C++", "Easy", rc == 0, out.strip(), err.strip()))

# P10 – Fibonacci
p10 = """\
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
"""
write_file(f"{BASE}/cpp/p10.cpp", p10)
rc, out, err = run("g++ -o p10 p10.cpp && ./p10", cwd=f"{BASE}/cpp")
results.append(("P10", "C++", "Easy", rc == 0, out.strip(), err.strip()))

# P11 – Swap by reference
p11 = """\
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
"""
write_file(f"{BASE}/cpp/p11.cpp", p11)
rc, out, err = run("g++ -o p11 p11.cpp && ./p11", cwd=f"{BASE}/cpp")
results.append(("P11", "C++", "Easy", rc == 0, out.strip(), err.strip()))

# P23 – Singly linked list
p23 = """\
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
"""
write_file(f"{BASE}/cpp/p23.cpp", p23)
rc, out, err = run("g++ -o p23 p23.cpp && ./p23", cwd=f"{BASE}/cpp")
results.append(("P23", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P24 – Deep vs shallow copy
p24 = """\
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
    MyString(const MyString& other) {
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
        cout << "[Deep Copy constructor called]" << endl;
    }
    void display() const {
        cout << "Data: " << data << " (address: " << (void*)data << ")" << endl;
    }
    ~MyString() { delete[] data; }
};

int main() {
    MyString original("Hello");
    MyString copy(original);
    cout << "Original: "; original.display();
    cout << "Copy:     "; copy.display();
    strcpy(copy.data, "World");
    cout << "\\nAfter modifying copy:" << endl;
    cout << "Original: "; original.display();
    cout << "Copy:     "; copy.display();
    return 0;
}
"""
write_file(f"{BASE}/cpp/p24.cpp", p24)
rc, out, err = run("g++ -o p24 p24.cpp && ./p24", cwd=f"{BASE}/cpp")
results.append(("P24", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P25 – std::sort with lambda
p25 = """\
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
"""
write_file(f"{BASE}/cpp/p25.cpp", p25)
rc, out, err = run("g++ -std=c++17 -o p25 p25.cpp && ./p25", cwd=f"{BASE}/cpp")
results.append(("P25", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P26 – Tower of Hanoi (added <cmath> for pow)
p26 = """\
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
    cout << "\\nTotal moves: " << (int)(pow(2, n) - 1) << endl;
    return 0;
}
"""
write_file(f"{BASE}/cpp/p26.cpp", p26)
rc, out, err = run("g++ -o p26 p26.cpp && ./p26", cwd=f"{BASE}/cpp")
results.append(("P26", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P27 – File I/O (create input.txt first)
write_file(f"{BASE}/cpp/input.txt", "Line one\nLine two\nLine three\nLine four\nLine five\n")
p27 = """\
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
        outFile << l << "\\n";
    }
    outFile.close();

    cout << "Done. Reversed content written to '" << outputFile << "'" << endl;
    return 0;
}
"""
write_file(f"{BASE}/cpp/p27.cpp", p27)
rc, out, err = run("g++ -o p27 p27.cpp && ./p27", cwd=f"{BASE}/cpp")
results.append(("P27", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P28 – std::map phonebook
p28 = """\
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

    cout << "\\nFull Phonebook:" << endl;
    for (const auto& [key, value] : phonebook) {
        cout << "  " << key << ": " << value << endl;
    }

    phonebook.erase("Bob");
    cout << "\\nAfter deleting Bob:" << endl;
    for (const auto& [key, value] : phonebook) {
        cout << "  " << key << ": " << value << endl;
    }
    return 0;
}
"""
write_file(f"{BASE}/cpp/p28.cpp", p28)
rc, out, err = run("g++ -std=c++17 -o p28 p28.cpp && ./p28", cwd=f"{BASE}/cpp")
results.append(("P28", "C++", "Medium", rc == 0, out.strip(), err.strip()))

# P40 – Memory leak fix
p40 = """\
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
"""
write_file(f"{BASE}/cpp/p40.cpp", p40)
rc, out, err = run("g++ -std=c++14 -o p40 p40.cpp && ./p40", cwd=f"{BASE}/cpp")
results.append(("P40", "C++", "Hard", rc == 0, out.strip(), err.strip()))

# P41 – unique_ptr / shared_ptr
p41 = """\
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class ResourceUnique {
    unique_ptr<int[]> data;
public:
    ResourceUnique(int size) : data(make_unique<int[]>(size)) {
        cout << "Unique resource acquired" << endl;
    }
};

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
        shared_ptr<SharedConfig> config2 = config1;
        cout << "Inside scope, ref count: " << config1.use_count() << endl;
    }
    cout << "Outside scope, ref count: " << config1.use_count() << endl;
    return 0;
}
"""
write_file(f"{BASE}/cpp/p41.cpp", p41)
rc, out, err = run("g++ -std=c++14 -o p41 p41.cpp && ./p41", cwd=f"{BASE}/cpp")
results.append(("P41", "C++", "Hard", rc == 0, out.strip(), err.strip()))

# P42 – Producer-consumer
p42 = """\
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
        cout << "[Producer] Produced: " << i << " (buffer size: " << buffer.size() << ")" << endl;
        lock.unlock();
        cv.notify_all();
        this_thread::sleep_for(chrono::milliseconds(10));
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
        this_thread::sleep_for(chrono::milliseconds(15));
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
"""
write_file(f"{BASE}/cpp/p42.cpp", p42)
rc, out, err = run("g++ -std=c++14 -pthread -o p42 p42.cpp && ./p42", cwd=f"{BASE}/cpp", timeout=20)
results.append(("P42", "C++", "Hard", rc == 0, out.strip(), err.strip()))

# P43 – Dangling pointer fix
p43 = """\
#include <iostream>
#include <memory>
using namespace std;

void fix_scope() {
    int x = 10;
    int* p = &x;
    cout << "Value: " << *p << endl;
}

void fix_heap() {
    int* p = new int(10);
    cout << "Value: " << *p << endl;
    delete p;
}

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
"""
write_file(f"{BASE}/cpp/p43.cpp", p43)
rc, out, err = run("g++ -std=c++14 -o p43 p43.cpp && ./p43", cwd=f"{BASE}/cpp")
results.append(("P43", "C++", "Hard", rc == 0, out.strip(), err.strip()))

# P44 – Rule of Three MyString
p44 = """\
#include <iostream>
#include <cstring>
using namespace std;

class MyString {
private:
    char* data;
    size_t length;
public:
    MyString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "[Constructor] \\"" << data << "\\"" << endl;
    }
    ~MyString() {
        cout << "[Destructor] \\"" << data << "\\"" << endl;
        delete[] data;
    }
    MyString(const MyString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "[Copy Constructor] \\"" << data << "\\"" << endl;
    }
    MyString& operator=(const MyString& other) {
        if (this == &other) return *this;
        delete[] data;
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "[Copy Assignment] \\"" << data << "\\"" << endl;
        return *this;
    }
    const char* c_str() const { return data; }
    size_t size() const { return length; }
};

int main() {
    MyString s1("Hello");
    MyString s2 = s1;
    MyString s3("World");
    s3 = s1;
    cout << "\\nValues: " << s1.c_str() << ", " << s2.c_str() << ", " << s3.c_str() << endl;
    return 0;
}
"""
write_file(f"{BASE}/cpp/p44.cpp", p44)
rc, out, err = run("g++ -o p44 p44.cpp && ./p44", cwd=f"{BASE}/cpp")
results.append(("P44", "C++", "Hard", rc == 0, out.strip(), err.strip()))

# ─────────────────────────────────────────────
#  JAVA PROMPTS
# ─────────────────────────────────────────────

def run_java(pid, classname, src, extra_flags=""):
    d = f"{BASE}/java/{pid}"
    os.makedirs(d, exist_ok=True)
    write_file(f"{d}/{classname}.java", src)
    rc, out, err = run(f"javac {extra_flags} {classname}.java && java {classname}", cwd=d, timeout=20)
    return rc, out, err

# P12 – Hello World + date
p12_src = """\
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
"""
rc, out, err = run_java("p12", "Main", p12_src)
results.append(("P12", "Java", "Easy", rc == 0, out.strip(), err.strip()))

# P13 – ArrayList forEach
p13_src = """\
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
"""
rc, out, err = run_java("p13", "Main", p13_src)
results.append(("P13", "Java", "Easy", rc == 0, out.strip(), err.strip()))

# P14 – isPrime
p14_src = """\
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
"""
rc, out, err = run_java("p14", "Main", p14_src)
results.append(("P14", "Java", "Easy", rc == 0, out.strip(), err.strip()))

# P15 – NullPointerException handling
p15_src = """\
public class Main {
    public static void main(String[] args) {
        String text = null;
        try {
            int length = text.length();
            System.out.println("Length: " + length);
        } catch (NullPointerException e) {
            System.out.println("Caught NullPointerException: The string is null.");
            System.out.println("Details: " + e.getMessage());
        } finally {
            System.out.println("Finally block always executes.");
        }
        String safeText = (text != null) ? text : "default";
        System.out.println("Safe value: " + safeText);
    }
}
"""
rc, out, err = run_java("p15", "Main", p15_src)
results.append(("P15", "Java", "Easy", rc == 0, out.strip(), err.strip()))

# P16 – Car class
p16_src = """\
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
"""
rc, out, err = run_java("p16", "Car", p16_src)
results.append(("P16", "Java", "Easy", rc == 0, out.strip(), err.strip()))

# P29 – ArrayStack
p29_src = """\
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
        if (top == capacity - 1) throw new RuntimeException("Stack overflow: stack is full.");
        stack[++top] = value;
        System.out.println("Pushed: " + value);
    }
    public int pop() {
        if (isEmpty()) throw new RuntimeException("Stack underflow: stack is empty.");
        return stack[top--];
    }
    public int peek() {
        if (isEmpty()) throw new RuntimeException("Stack is empty.");
        return stack[top];
    }
    public boolean isEmpty() { return top == -1; }
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
"""
rc, out, err = run_java("p29", "ArrayStack", p29_src)
results.append(("P29", "Java", "Medium", rc == 0, out.strip(), err.strip()))

# P30 – Method overriding ShapeDemo
p30_src = """\
public class ShapeDemo {
    static class Shape {
        public double calculateArea() { return 0.0; }
        public String describe() { return "I am a Shape with area: " + calculateArea(); }
    }
    static class Circle extends Shape {
        private double radius;
        public Circle(double radius) { this.radius = radius; }
        @Override
        public double calculateArea() { return Math.PI * radius * radius; }
        @Override
        public String toString() {
            return String.format("Circle (radius=%.2f) -> Area: %.4f", radius, calculateArea());
        }
    }
    static class Rectangle extends Shape {
        private double width, height;
        public Rectangle(double width, double height) { this.width = width; this.height = height; }
        @Override
        public double calculateArea() { return width * height; }
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
"""
rc, out, err = run_java("p30", "ShapeDemo", p30_src)
results.append(("P30", "Java", "Medium", rc == 0, out.strip(), err.strip()))

# P31 – Array intersection
p31_src = """\
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
        Arrays.sort(result);
        System.out.println("Intersection: " + Arrays.toString(result));
    }
}
"""
rc, out, err = run_java("p31", "ArrayIntersection", p31_src)
results.append(("P31", "Java", "Medium", rc == 0, out.strip(), err.strip()))

# P32 – Interface InstrumentDemo
p32_src = """\
public class InstrumentDemo {
    interface Playable {
        void play();
        default String getType() { return "Unknown Instrument"; }
    }
    static class Guitar implements Playable {
        private String brand;
        public Guitar(String brand) { this.brand = brand; }
        @Override
        public void play() { System.out.println(brand + " Guitar: Strumming chords..."); }
        @Override
        public String getType() { return "String Instrument"; }
    }
    static class Piano implements Playable {
        @Override
        public void play() { System.out.println("Piano: Playing a melody..."); }
    }
    public static void main(String[] args) {
        Playable[] instruments = { new Guitar("Fender"), new Piano() };
        for (Playable instrument : instruments) {
            instrument.play();
            System.out.println("  Type: " + instrument.getType());
        }
    }
}
"""
rc, out, err = run_java("p32", "InstrumentDemo", p32_src)
results.append(("P32", "Java", "Medium", rc == 0, out.strip(), err.strip()))

# P33 – Anagram check
p33_src = """\
import java.util.Arrays;

public class AnagramCheck {
    public static boolean isAnagram(String s1, String s2) {
        if (s1 == null || s2 == null) return false;
        s1 = s1.replaceAll("\\\\s+", "").toLowerCase();
        s2 = s2.replaceAll("\\\\s+", "").toLowerCase();
        if (s1.length() != s2.length()) return false;
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
        return Arrays.equals(c1, c2);
    }
    public static void main(String[] args) {
        System.out.println(isAnagram("listen", "silent"));
        System.out.println(isAnagram("Astronomer", "Moon starer"));
        System.out.println(isAnagram("hello", "world"));
        System.out.println(isAnagram("Dormitory", "Dirty room"));
    }
}
"""
rc, out, err = run_java("p33", "AnagramCheck", p33_src)
results.append(("P33", "Java", "Medium", rc == 0, out.strip(), err.strip()))

# P45 – DatabaseConnection Singleton
p45_src = """\
public class DatabaseConnection {
    private volatile static DatabaseConnection instance;
    private String connectionString;
    private DatabaseConnection() {
        this.connectionString = "jdbc:mysql://localhost:3306/mydb";
        System.out.println("DatabaseConnection created (id: " + System.identityHashCode(this) + ")");
    }
    public static DatabaseConnection getInstance() {
        if (instance == null) {
            synchronized (DatabaseConnection.class) {
                if (instance == null) {
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
    public String getConnectionString() { return connectionString; }
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
"""
rc, out, err = run_java("p45", "DatabaseConnection", p45_src)
results.append(("P45", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# P46 – Deadlock demo (safe version only)
p46_src = """\
public class DeadlockDemo {
    static final Object LOCK_A = new Object();
    static final Object LOCK_B = new Object();
    static class SafeThread1 implements Runnable {
        public void run() {
            synchronized (LOCK_A) {
                synchronized (LOCK_B) {
                    System.out.println("SafeThread1: both locks acquired");
                }
            }
        }
    }
    static class SafeThread2 implements Runnable {
        public void run() {
            synchronized (LOCK_A) {
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
"""
rc, out, err = run_java("p46", "DeadlockDemo", p46_src)
results.append(("P46", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# P47 – Stream API + records
p47_src = """\
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
"""
rc, out, err = run_java("p47", "EmployeeAnalysis", p47_src)
results.append(("P47", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# P48 – BST delete
p48_src = """\
public class BST {
    private static class Node {
        int value;
        Node left, right;
        Node(int val) { this.value = val; }
    }
    private Node root;
    public void insert(int val) { root = insertRec(root, val); }
    private Node insertRec(Node node, int val) {
        if (node == null) return new Node(val);
        if (val < node.value) node.left = insertRec(node.left, val);
        else if (val > node.value) node.right = insertRec(node.right, val);
        return node;
    }
    public void delete(int val) { root = deleteRec(root, val); }
    private Node deleteRec(Node node, int val) {
        if (node == null) return null;
        if (val < node.value) { node.left = deleteRec(node.left, val); }
        else if (val > node.value) { node.right = deleteRec(node.right, val); }
        else {
            if (node.left == null && node.right == null) return null;
            if (node.left == null) return node.right;
            if (node.right == null) return node.left;
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
    public void inorder() { inorderRec(root); System.out.println(); }
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
        tree.delete(20);
        System.out.print("After deleting 20: "); tree.inorder();
        tree.delete(30);
        System.out.print("After deleting 30: "); tree.inorder();
        tree.delete(50);
        System.out.print("After deleting 50: "); tree.inorder();
    }
}
"""
rc, out, err = run_java("p48", "BST", p48_src)
results.append(("P48", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# P49 – SRP OrderProcessor with records
p49_src = """\
import java.util.*;

public class OrderProcessor {
    record Order(int id, List<Double> items, String customerEmail, String coupon) {}
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
        if (!validator.validate(order)) { System.out.println("Error: invalid order"); return; }
        double subtotal = calculator.calculateSubtotal(order.items());
        subtotal = calculator.applyDiscount(subtotal, order.coupon());
        double total = calculator.applyTax(subtotal, 0.08);
        emailService.sendConfirmation(order.customerEmail(), total);
        logger.log(order.id());
    }
    public static void main(String[] args) {
        Order order = new Order(101, List.of(29.99, 49.99, 14.99), "alice@example.com", "SAVE10");
        processOrder(order);
    }
}
"""
rc, out, err = run_java("p49", "OrderProcessor", p49_src)
results.append(("P49", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# P50 – Dijkstra
p50_src = """\
import java.util.*;

public class Dijkstra {
    static final int INF = Integer.MAX_VALUE;
    public static int[] dijkstra(int[][] graph, int source) {
        int n = graph.length;
        int[] dist = new int[n];
        boolean[] visited = new boolean[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;
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
"""
rc, out, err = run_java("p50", "Dijkstra", p50_src)
results.append(("P50", "Java", "Hard", rc == 0, out.strip(), err.strip()))

# ─────────────────────────────────────────────
#  WRITE RESULTS FILE
# ─────────────────────────────────────────────
passed = sum(1 for r in results if r[3])
failed = len(results) - passed

lines = []
lines.append("# Execution Results – 50 Coding Prompts")
lines.append(f"**Date:** 2026-05-12  ")
lines.append(f"**Environment:** Python 3.13, Apple Clang 16, OpenJDK 25  ")
lines.append(f"**Total:** {len(results)} | **Passed:** {passed} | **Failed:** {failed}")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary Table")
lines.append("")
lines.append("| ID | Language | Difficulty | Status | Output (truncated) |")
lines.append("|----|----------|------------|--------|--------------------|")

for pid, lang, diff, ok, out, err in results:
    status = "✅ PASS" if ok else "❌ FAIL"
    preview = (out[:80].replace("\n", " ") if ok else err[:80].replace("\n", " "))
    lines.append(f"| {pid} | {lang} | {diff} | {status} | `{preview}` |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## Detailed Output")
lines.append("")

for pid, lang, diff, ok, out, err in results:
    status = "PASS" if ok else "FAIL"
    lines.append(f"### {pid} | {lang} ({diff}) — {status}")
    if out:
        lines.append("**stdout:**")
        lines.append("```")
        lines.append(out[:500])
        lines.append("```")
    if err:
        lines.append("**stderr:**")
        lines.append("```")
        lines.append(err[:300])
        lines.append("```")
    lines.append("")

out_path = "/Volumes/Untitled/claude test for 659/execution_results.md"
with open(out_path, "w") as f:
    f.write("\n".join(lines))

print(f"Done. {passed}/{len(results)} passed.")
print(f"Results saved to: {out_path}")
for pid, lang, diff, ok, out, err in results:
    mark = "PASS" if ok else "FAIL"
    print(f"  {pid} [{lang}/{diff}]: {mark}")
