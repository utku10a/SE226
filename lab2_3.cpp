#include <iostream>
#include <string>
using namespace std;

int main () {

    int n;
    cout << "Enter a number between 3 - 9:";
    cin >> n;

    string s = "";
    for (int i = 1; i < n + 1; i++) {
        s += to_string(i);
        cout << s << endl;
    }
    for (int i = n; i >= 1; i--) {
        s.pop_back();
        cout << s << endl;
    }
    return 0;

}