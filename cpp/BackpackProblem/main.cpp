#include <iostream>
#include <fstream>

using namespace std;

void backpack(int **arr, int **items, int cost[], int weight[], int n, int w)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= w; j++)
        {
            if (weight[i - 1] <= j)
            {
                arr[i][j] = max(arr[i - 1][j], cost[i - 1] + arr[i - 1][j - weight[i - 1]]);
                items[i][j] = i;
            }
            else
            {
                arr[i][j] = arr[i - 1][j];
                items[i][j] = items[i - 1][j];
            }
        }
    }
}

void find_the_best(int **arr, int **items, int weight[], int n, int w, ofstream &OutputFile)
{
    int the_best = arr[n][w];
    while (arr[n][w] == the_best)
    {
        int help_w = w;
        while (help_w > 0)
        {
            OutputFile << items[n][help_w] << " ";
            help_w -= weight[items[n][help_w] - 1];
        }
        OutputFile << endl;
        n--;
    }
}

int main()
{
    int n, w;
    ifstream InputFile("In0302.txt");
    InputFile >> n >> w;
    int *cost = new int[n];
    int *weight = new int[n];
    int **arr;
    int **items;
    arr = new int *[n];

    for (int i = 0; i <= n; i++)
    {
        arr[i] = new int[w + 1];
    }
    items = new int *[n];

    for (int i = 0; i <= n; i++)
    {
        items[i] = new int[w + 1];
    }

    for (int i = 0; i < n; i++)
    {
        InputFile >> cost[i] >> weight[i];
    }
    InputFile.close();

    backpack(arr, items, cost, weight, n, w);

    ofstream OutputFile("Out0302.txt");
    find_the_best(arr, items, weight, n, w, OutputFile);

    OutputFile.close();
    return 0;
}