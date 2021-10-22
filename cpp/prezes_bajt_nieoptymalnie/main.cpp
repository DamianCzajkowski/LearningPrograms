#include <iostream>
#include <fstream>

using namespace std;

int main()
{
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
    ofstream OutputFile("Out0103.txt");
    OutputFile << f_idx << " " << l_idx << " " << result;
    OutputFile.close();
    // O(n^2)
}