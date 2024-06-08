#include <iostream>

using namespace std;

void teachphy(int hours){
    for(int i = 1; i <= hours; i++){
        cout << "I am your teacher" << endl;
    }
}

int main(){
    cout << "Hello World" << endl;
    teachphy(5);
    return 1;
}