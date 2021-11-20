#include <iostream>
#include <fstream>

using namespace std;

void magicSquare(char **arr, int n, int idx, int idy, int &counter, string text)
{
    for (int j = idy; j <= n - idy; j++)
    {
        arr[idx][j] = text[counter % text.length()];
        counter++;
    }
    if (idy == n - idy)
    {
        return;
    }
    idy = n - idy;
    for (int i = idx + 1; i <= n - idx; i++)
    {
        arr[i][idy] = text[counter % text.length()];
        counter++;
    }
    idx = n - idx;
    for (int j = idy - 1; j >= n - idy; j--)
    {
        arr[idx][j] = text[counter % text.length()];
        counter++;
    }
    if (idy == n - idy + 1)
    {
        return;
    }
    idy = n - idy;
    idx--;
    for (int i = idx; i >= n - idx; i--)
    {
        arr[i][idy] = text[counter % text.length()];
        counter++;
    }
    idx = n - idx;
    idy++;
    magicSquare(arr, n, idx, idy, counter, text);
}

int main()
{
    int n;
    int counter = 0;
    string text;
    ifstream InputFile("In0206.txt");
    InputFile >> n >> text;
    InputFile.close();

    char ***arr;
    arr = new char **[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new char *[n];
        for (int j = 0; j < n; j++)
            arr[i][j] = new char[n];
    }
    for (int i = 0; i < n; i++)
    {
        magicSquare(arr[i], n - 1, 0, 0, counter, text);
    }

    ofstream OutputFile("Out0206.txt");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                OutputFile << arr[i][j][k] << ' ';
            }
            OutputFile << endl;
        }
        OutputFile << endl;
    }
    OutputFile.close();

    return 0;
}
