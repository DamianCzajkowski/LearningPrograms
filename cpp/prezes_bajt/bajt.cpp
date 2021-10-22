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
}