#include <iostream>
using namespace std;
// TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
int main() {
    int t_saniye;
    cout << "Enter time in seconds:";
    cin >> t_saniye;

    int hours = (t_saniye/3600);
int minutes = (t_saniye%3600)/60;
int seconds = (t_saniye%60);

cout << t_saniye <<" seconds is " << hours << " hours, " << minutes << " minutes and " << seconds << " seconds." << endl;

    return 0;
    // TIP See CLion help at <a href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>. Also, you can try interactive lessons for CLion by selecting 'Help | Learn IDE Features' from the main menu.
}