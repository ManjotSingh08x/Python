#include <iostream>
using namespace std;

int main(){
    char ch;
    cout << "Enter a character or number: ";
    cin >> ch;

    if (ch >= '0' && ch <= '9'){
        cout << "Numeric Value\n";
    }

    else if (ch >= 'a' && ch <= 'z'){
        cout << "Lowercase Value\n";
    }

    else if (ch >= 'A' && ch <= 'Z'){
        cout << "Uppercase Value\n";
    }
    else{
        cout << "No alphabet or number detected";
    }
    return 0;
}
