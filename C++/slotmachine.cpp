#include <iostream>

using namespace std;

int main(){
    srand(time(NULL));
    
    
    int k = 10;
    int krok = 0;
    int p;

    while (k > 0) {
        
        k--;
        krok++;
        p = 0;
        
        int x = 1 + rand() %6;
        int y = 1 + rand() %6;
        int z = 1 + rand() %6;
        
        if (x < y && y < z) {
            p = 1;
        }
        else if (x == y && y == z) {
            p = 3;
                if ( x == 6) {
                    p += 3;
                }
        }
        else if (x == y || x == y || y == z ) {
            p = 2;
        }
        
        k += p;

        cout << krok << "   " << x << " " << y << " " << z << "   " << p << "   " << k  << endl;
    }
    return 0;
}