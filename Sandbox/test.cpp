#include <iostream>
using namespace std;

int main() {
    for(int i = -127; i < 128; i++){
        char ch = i;
        cout << i << ": " << ch << endl;
    }
    return 0;
}