#include <iostream>

using namespace std;
int main()
{
    long long x = 1;
    long long n = 10;
    long long m = 1;

    for (int i = 2; i <= n; i++)
    {
        x = (x * i) % m;
    }
    cout << x % m << "\n";
}