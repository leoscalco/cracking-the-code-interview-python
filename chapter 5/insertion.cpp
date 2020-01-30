// #include <bits/stdc++>;
#include <iostream>
using namespace std;

int updateBits(long long int n, int m, int i, int j){
    int allOnes = ~0;

    int left = allOnes << (j+1);

    int right = ((1 << i) - 1);

    int mask = left | right;

    int n_cleared = n & mask;
    int m_shifted = m << 1;
    return n_cleared | m_shifted;
}

int main(){
    cout << updateBits(10000000000, 10011, 2, 6) << endl;
    return 0;
}