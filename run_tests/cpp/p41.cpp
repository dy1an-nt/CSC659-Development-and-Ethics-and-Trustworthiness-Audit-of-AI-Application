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
