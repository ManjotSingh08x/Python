#include <iostream>
using namespace std;

int main(){
    cout << "Entr a number: ";
    int n;

    cin >> n;

    if (n >0) {
        cout << "Your number is positive" << endl;
    } 
    else if (n < 0) {
        cout << "Your number is negative" << endl;
    }
    else {
        cout << "Your number is zero" << endl;
    }
}