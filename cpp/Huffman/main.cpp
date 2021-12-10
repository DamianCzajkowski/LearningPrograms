// https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

void frequency(char *letters, int *freq, string text, ofstream &OutputFile)
{
    int count[256] = {};
    for (int i = 0; text[i]; i++)
    {
        count[text[i]]++;
    }
    int j = 0;
    for (int i = 0; i < 256; i++)
    {
        if (count[i])
        {
            letters[j] = (char)i;
            freq[j] = count[i];
            OutputFile << (char)i << " " << count[i] << ", ";
            j++;
        }
    }
    OutputFile << endl;
}

// void huffman

int main()
{
    string text;
    ifstream InputFile("In0305.txt");
    getline(InputFile, text);
    InputFile.close();
    int len = text.length();
    char *letters = new char[len];
    int *freq = new int[len];

    ofstream OutputFile("Out0305.txt");
    frequency(letters, freq, text, OutputFile);
    OutputFile.close();
}
