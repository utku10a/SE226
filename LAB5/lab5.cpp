#include <iostream>
using namespace std;

int recursiveGeometric(int n, int r) {
    if (n == 0)
        return 1;

    return r * recursiveGeometric(n - 1, r) + 1;
}

int main() {
    int n, r;

    cout << "Enter n: ";
    cin >> n;

    cout << "Enter r: ";
    cin >> r;

    int sonuc = recursiveGeometric(n, r);

    cout << "Result: " << sonuc;

    return 0;
}
