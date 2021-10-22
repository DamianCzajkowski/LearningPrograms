#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    // ZADANIE 1.1
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

    // ZADANIE 1.5
    int n, k, counter = 0;

    ifstream InputFile("In0101.txt");
    InputFile >> n >> k;
    InputFile.close();

    int tab[n + 1][k + 1];

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= min(k, i); j++)
        {
            if (i == j || j == 0)
            {
                tab[i][j] = 1;
            }
            else
            {
                tab[i][j] = tab[i - 1][j - 1] + tab[i - 1][j];
                counter++;
            }
        }
    }

    int result = tab[n][k];

    ofstream OutputFile("Out0101.txt");
    OutputFile << "n=" << n << " k=" << k << endl;
    OutputFile << "SN5 = " << result << ", licz = " << counter;
    OutputFile.close();

    // ZADANIE 3 OPTYMALNIE

    int n;
    ifstream InputFile("In0103.txt");
    InputFile >> n;

    int tab[n];

    for (int i = 0; i < n; i++)
    {
        InputFile >> tab[i];
    }
    InputFile.close();

    int f_idx = 0, l_idx, result = 0;
    int local_sum = 0, local_l_idx = 0, local_f_idx;

    for (int i = 0; i < n; i++)
    {
        local_sum += tab[i];
        if (local_sum < 0)
        {
            local_sum = 0;
            local_f_idx = i + 2;
        }
        local_l_idx = i + 1;
        if (local_sum > result)
        {
            result = local_sum;
            l_idx = local_l_idx;
            f_idx = local_f_idx;
        }
    }
    ofstream OutputFile("Out0103.txt");
    OutputFile << f_idx << " " << l_idx << " " << result;
    OutputFile.close();
    // O(n)

    // ZADANIE 3 NIEOPTYMALNIE
    int n;
    ifstream InputFile("In0103.txt");
    InputFile >> n;

    int tab[n];

    for (int i = 0; i < n; i++)
    {
        InputFile >> tab[i];
    }
    InputFile.close();

    int f_idx = 0, l_idx, result = 0;
    int local_sum = 0;

    for (int i = 0; i < n; i++)
    {
        local_sum = 0;
        for (int j = i; j < n; j++)
        {
            local_sum += tab[j];
            if (local_sum > result)
            {
                result = local_sum;
                f_idx = i + 1;
                l_idx = j + 1;
            }
        }
    }
    ofstream OutputFile("Out01032.txt");
    OutputFile << f_idx << " " << l_idx << " " << result;
    OutputFile.close();
    // O(n^2)
}