#include <iostream>
#include <string>

using namespace std;

string number(int x){
    if (x == 0) {
        return "0";
    }
    int y = 1;
    while (y <= x){
        y = y * 2;
    }
    y = y / 2;
    int z = y;
    string bin = "1";
    
    while (y > 1){
        y = y / 2;
        if ( z + y <= x){
            bin += "1";
            z += y;
        }
        else {
            bin += "0";
        }
    }
    return bin;
}

int main(){
    
    cout << number(23411234);
}