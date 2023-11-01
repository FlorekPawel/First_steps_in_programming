#include <iostream>
#include <cmath>
using namespace std;

int main () {
    int dzień = 1;
    int kury = 200;
    float zysk = 0;
    int jajka = 0;
    int nowe_kury;
    int dzień_jaj;
    
    while (dzień <= 180){
        zysk -= kury * 0.2 * 1.9;

        if (dzień % 7 != 0) {
            jajka += kury;
            zysk += kury * 0.9;
        }
        if (dzień % 30 == 0) {
            nowe_kury = floor(kury * 0.2);
            zysk -= nowe_kury * 18;
            kury += nowe_kury;
        }
        if (dzień % 2 == 0){
            kury -= 2;
        }
        
        cout << dzień << "\t" << kury << "\t" << jajka << "\t" << zysk << endl;
        
        if (jajka <= 3000){
            dzień_jaj = dzień;
        } 
        dzień++;
    }
    cout << dzień_jaj + 1 << " dnia liczba sprzedanych jaj przekroczyla 3000" << endl;
        
}