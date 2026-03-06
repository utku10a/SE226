#include <iostream>
using namespace std;

int main() {
    int count = 0;
int n;
    cout << "Please enter a positive integer greater than 9:";
    cin >> n;

    while (n >= 10) {
     int temp = n;
        int sum = 0;
        while (temp > 0) {
            sum += temp % 10;
            temp = temp / 10;
        }
        cout << n << "=>" << sum << endl;
        n = sum;
        count++;
    }
    cout << "Last value: " << n << endl;
    cout << "Total steps: " << count << endl;

return 0;
}