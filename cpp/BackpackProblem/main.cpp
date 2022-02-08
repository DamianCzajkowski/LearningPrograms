#include <iostream>
#include <fstream>

using namespace std;

void backpack(int **arr, int **zero_one_arr, int cost[], int weight[], int n, int w)
{
    int pom;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= w; j++)
        {
            if (weight[i - 1] <= j)
            {
                pom = cost[i - 1] + arr[i - 1][j - weight[i - 1]];
                if (pom < arr[i - 1][j])
                {
                    arr[i][j] = arr[i - 1][j];
                }
                else
                {
                    arr[i][j] = pom;
                    zero_one_arr[i][j] = 1;
                }
            }
            else
            {
                arr[i][j] = arr[i - 1][j];
            }
        }
    }
}

void find_the_best(int **arr, int **zero_one_arr, int weight[], int n, int w, ofstream &OutputFile)
{
    int the_best = arr[n][w];
    int counter = n;
    while (arr[counter][w] == the_best)
    {
        int help_w = w;
        if (!zero_one_arr[counter][help_w])
        {
            counter = --n;
            continue;
        }
        while (help_w > 0)
        {
            if (zero_one_arr[counter][help_w])
            {
                OutputFile << counter << " ";
                help_w -= weight[counter - 1];
            }
            else
            {
                counter--;
            }
        }
        OutputFile << endl;
        counter = --n;
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
    int **zero_one_arr;
    arr = new int *[n];

    for (int i = 0; i <= n; i++)
    {
        arr[i] = new int[w + 1];
    }
    zero_one_arr = new int *[n];

    for (int i = 0; i <= n; i++)
    {
        zero_one_arr[i] = new int[w + 1];
        for (int j = 0; j <= n; j++)
        {
            zero_one_arr[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++)
    {
        InputFile >> cost[i] >> weight[i];
    }
    InputFile.close();

    backpack(arr, zero_one_arr, cost, weight, n, w);

    ofstream OutputFile("Out0302.txt");
    find_the_best(arr, zero_one_arr, weight, n, w, OutputFile);

    OutputFile.close();
    return 0;
}