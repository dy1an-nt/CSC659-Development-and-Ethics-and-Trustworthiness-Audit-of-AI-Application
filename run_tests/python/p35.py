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
