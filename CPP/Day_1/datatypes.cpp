#include <iostream>
using namespace std;

int main(){
    int number = 5;
    cout << "Value of a is " << number << " & size of a is " << sizeof(number) << endl;
    char ch = 'a';
    cout << "Value of ch is " << ch << " & size of ch is " << sizeof(ch) << endl;
    // Learning operations
    int a = 5;
    int b = 2;
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    // Take special care in division
    cout << "a / b = " << a / b << endl;
    cout << "a / b (in float) " << (float)a/b << endl;
    cout << "a % b = " << a % b << endl;
    return 1;
}