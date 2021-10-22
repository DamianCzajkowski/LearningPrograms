#include <iostream>
#include <fstream>

using namespace std;

int main()
{

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
}
