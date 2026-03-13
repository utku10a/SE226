#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {

    cout << "Before swap:\na = " << *p1 << "\nb = " << *p2 << endl;

    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;

    cout << "After swap:\na = " << *p1 << "\nb = " << *p2 << endl;

}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";;
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    int max = arr[0];
    for (int i = 0; i < size; i++) {
     if (arr[i] > max) {
         max = arr[i];
     }
    }
    cout << "Maximum element: " << max << endl;
    return max;
}

int* createArray(int size) {
    cout << "Creating dynamic array..." << endl;
   int* arr = new int[size];
    return arr;
}

void deleteArray(int* arr) {
    cout << "Deleting array...\nMemory released successfully." << endl;
    delete[] arr;
}

void reverseArray(int* arr, int size) {
    int left = 0, right = size - 1;
    while (left < right) {
        swapValues(&arr[left], &arr[right]);
        ++left;
        --right;
    }
    cout << "Reversing array...\n\nArray after reverseArray (printArray method comes here in main):" << endl;
}
int main () {
    int arr[5] = {1, 2, 3, 100000, 8};
    return 0;
}

