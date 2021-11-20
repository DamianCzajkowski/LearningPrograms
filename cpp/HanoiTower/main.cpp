#include <iostream>
#include <fstream>

using namespace std;

void hanoiTower(int n, int from_stick, int to_stick, int help_stick, ofstream &OutputFile)
{
    if (n == 1)
    {
        OutputFile << from_stick << "->" << to_stick << ", ";
        return;
    }
    hanoiTower(n - 1, from_stick, help_stick, to_stick, OutputFile);
    OutputFile << from_stick << "->" << to_stick << ", ";
    hanoiTower(n - 1, help_stick, to_stick, from_stick, OutputFile);
}

int main()
{
    int n;
    ifstream InputFile("In0204.txt");
    InputFile >> n;
    InputFile.close();

    ofstream OutputFile("Out0204.txt");
    OutputFile << "N=" << n << endl;
    hanoiTower(n, 1, 2, 3, OutputFile);
    OutputFile.close();
}
