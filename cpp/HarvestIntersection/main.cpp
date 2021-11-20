#include <iostream>
#include <fstream>

using namespace std;

int binarySearch(int tab[], int value, int start, int end)
{
    if (end >= start)
    {
        int middle = (start + end) / 2;
        if (tab[middle] == value)
        {
            return value;
        }
        else if (tab[middle] < value)
        {
            return binarySearch(tab, value, middle + 1, end);
        }
        else if (tab[middle] > value)
        {
            return binarySearch(tab, value, start, middle - 1);
        }
    }

    return 0;
}

int *harvestIntersection(int first_tab[], int second_tab[], int n, int &new_tab_len)
{
    int *new_tab = new int[n];
    int var;
    for (int i = 0; i < n; i++)
    {
        var = binarySearch(second_tab, first_tab[i], 0, n - 1);
        if (var > 0)
        {
            new_tab[new_tab_len] = var;
            new_tab_len++;
        }
    }
    return new_tab;
}

int main()
{
    int n, new_tab_len = 0;
    ifstream InputFile("In0207.txt");
    InputFile >> n;

    int *first_tab = new int[n];
    int *second_tab = new int[n];
    int *new_tab;

    for (int i = 0; i < n; i++)
    {
        InputFile >> first_tab[i];
    }
    for (int i = 0; i < n; i++)
    {
        InputFile >> second_tab[i];
    }
    InputFile.close();

    new_tab = harvestIntersection(first_tab, second_tab, n, new_tab_len);

    ofstream OutputFile("Out0207.txt");
    for (int i = 0; i < new_tab_len; i++)
    {
        OutputFile << new_tab[i] << ' ';
    }
    OutputFile << endl
               << new_tab_len;

    OutputFile.close();
}