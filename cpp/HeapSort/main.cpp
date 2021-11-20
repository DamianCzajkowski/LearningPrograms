#include <iostream>
#include <fstream>

using namespace std;

void heapify(int *arr, int heap_size, int i)
{
    int left = (i + 1 << 1) - 1;
    int right = (i + 1 << 1);
    int largest;
    if (left <= heap_size && arr[left] > arr[i])
    {
        largest = left;
    }
    else
    {
        largest = i;
    }
    if (right <= heap_size && arr[right] > arr[largest])
    {
        largest = right;
    }
    if (largest != i)
    {
        int help_var = arr[i];
        arr[i] = arr[largest];
        arr[largest] = help_var;
        heapify(arr, heap_size, largest);
    }
}

void buildHeap(int *arr, int n)
{
    for (int i = (n / 2) - 1; i >= 0; i--)
    {
        heapify(arr, n - 1, i);
    }
}

void heapSort(int *arr, int n)
{
    buildHeap(arr, n);
    for (int i = n; i >= 1; i--)
    {
        int help_var = arr[0];
        arr[0] = arr[i];
        arr[i] = help_var;
        n--;
        heapify(arr, n, 0);
    }
}

int main()
{
    int n;
    ifstream InputFile("In0201.txt");
    InputFile >> n;

    int *tab = new int[n];

    for (int i = 0; i < n; i++)
    {
        InputFile >> tab[i];
    }
    InputFile.close();

    heapSort(tab, n - 1);

    ofstream OutputFile("Out0201.txt");
    for (int i = 0; i < n; i++)
    {
        OutputFile << tab[i] << ' ';
    }

    OutputFile.close();
}