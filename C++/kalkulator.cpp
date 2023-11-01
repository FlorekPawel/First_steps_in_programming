#include <iostream>

using namespace std;

int main() {
    float x, y, res;
    char c;

    while (1) {
        cout << "Działanie: ";
        cin >> x >> c >> y;

        switch (c) {
            case "+":
                res = x + y;
            case "-":
                res = x - y;
            case "/":
                res = x / y;
            case "*":
                res = x * y;
        }

        cout << endl << res << endl;
    }
}