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
