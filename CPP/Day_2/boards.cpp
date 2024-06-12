#include <iostream>
using namespace std;

int main(){
    int phy, chem, maths;

    cout << "Enter your physics marks: ";
    cin >> phy;

    cout << "Enter your chemistry marks: ";
    cin >> chem;

    cout << "Enter your maths marks: ";
    cin >> maths;
    
    if (phy >= 33 && chem >= 33 && maths >= 33){
        cout << "You have PASSED!" << endl;
        float percentage = (float)(phy + chem + maths)/3 ;
        
        if (percentage >= 75){
            cout << "Qualified for jee mains " << '(' << percentage << ')'<< endl;
        }
        else{
            cout << "Not Qualified " << '(' << percentage << ')' << endl;
        }
    } 
    else{
        cout << "you have FAILED" << endl;
    }


}