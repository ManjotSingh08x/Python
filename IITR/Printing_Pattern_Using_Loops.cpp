#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n ; cin >> n;
    int length = 2 * n - 1;
    int row[length];
    for(int i = 0; i < length; i++){
        row[i] = n;
    }
    for(int i = 1; i < n; i++){
        for(int j = 0; j < length; j++){
            cout << row[j] << ' ';
        }
        for(int j = i; j < length - i; j++){
            row[j]--;
        }
        cout << '\n';

    }
    for(int i = n-1; i >= 0; i--){
        for(int j = 0; j < length; j++){
            cout << row[j] << ' ';
        }
        for(int j = i; j < length - i; j++){
            row[j]++;
        }
        cout << '\n';

    }
}
int main() {
    solve();
    return 0;
}