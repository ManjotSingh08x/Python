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
    // by doing int/int we get an integer hence 5/2 = 2.5 -> 2 in output
    // to return a float, we need to express numerator as a float
    // float/ int returns float and double/int returns double
    cout << "a / b = " << a / b << endl;
    cout << "a / b (in float) " << (float)a / b << endl;
    cout << "a % b = " << a % b << endl;

    //displaying relational operation
    cout << "a < b: " << (a < b) << endl; // false
    cout << "a > b: " << (a > b) << endl; // true
    cout << "a <= b: " << (a <= b) << endl; // false
    cout << "a >= b: " << (a >= b) << endl; // true 
    cout << "a != b: " << (a != b) << endl; // true 
    cout << "a == b: " << (a == b) << endl; // false

    // to convert a lowercase letter into uppercase letter we use this technique
    char char1 = 'h';
    cout << "Initially char1 is " << char1 << endl;
    char1 = char1 + 'A' - 'a'; // Does bitshifting to retrun ascii position of capital B
    cout << "Finally char1 is " << char1 << endl;
    return 1;
}