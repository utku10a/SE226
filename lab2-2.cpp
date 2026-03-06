#include <iostream>
using namespace std;
int main() {

    int n;
    cout << "Please enter a positive integer between 10 and 100:";
    cin >> n;

    for (int i = 1; i <= n; i++) {
    if (i % 3) {
     cout << "Fizz" << endl;
    } else
        if (i % 5 == 0) {
            cout << "Buzz" << endl;
    } else {
        cout << i << endl;
    }

    }

    return 0;
}