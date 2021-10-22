#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    // pattern for newton is n!/k!(n-k)!
    int n, k, counter = 0;

    ifstream InputFile("In0101.txt");
    InputFile >> n >> k;
    InputFile.close();
    if (n > 20 || k > 20)
    {
        cout << "Uwaga z taką wartością 'n' przekroczysz maksymalną pojemność zmiennej typu long long";
        return 0;
    }
    long long n_factorial = 1;
    for (int i = 2; i <= n; i++)
    {
        n_factorial *= i;
        counter++;
    }

    long long k_factorial = 1;
    for (int i = 2; i <= k; i++)
    {
        k_factorial *= i;
        counter++;
    }

    long long n_m_k_factorial = 1;
    for (int i = 2; i <= n - k; i++)
    {
        n_m_k_factorial *= i;
        counter++;
    }

    long long result = n_factorial / (k_factorial * n_m_k_factorial);
    counter++;

    ofstream OutputFile("Out0101.txt");
    OutputFile << "n=" << n << " k=" << k << endl;
    OutputFile << "SN1 = " << result << ", licz = " << counter;
    OutputFile.close();
    // O(n)
}