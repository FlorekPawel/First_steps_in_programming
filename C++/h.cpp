#include <iostream>
#include <cmath>
using namespace std;

int main() {
    
    cout << "Podaj l. nieparz: ";
    int n;
    cin >> n;
    while (n % 2 == 0) {
        cout << "To nie jest l. nieparz, podaj jeszcze raz: ";
        cin >> n;
    }
    for (int j = 1; j <= n; j++){
        if (j == 0.5 * n + 0.5){
            for (int k = 1; k <= n; k++){
                if (k == n) cout << "H\n";
                else cout << "H ";
            }
        }
        else {    
            for (int i = 1; i <= n; i++) {   
                if (i == 1) cout << "H ";
                else if (i == n) cout << "H\n";
                else cout << "  ";
            }
        }
    }
}
