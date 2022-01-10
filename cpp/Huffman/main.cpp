// https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

struct Node
{
    char ch;
    unsigned int freq;
    Node *left, *right;
    Node(char c, unsigned int f, Node *l = NULL, Node *r = NULL)
    {
        this->freq = f;
        this->ch = c;
        this->left = l;
        this->right = r;
    }
};

struct compare
{
    bool operator()(Node *l, Node *r)
    {
        return l->freq > r->freq;
    }
};

void print_codes(Node *root, string str, ofstream &OutputFile)
{
    if (root->ch != '$')
    {
        OutputFile << root->ch << " " << str << " ";
        return;
    }
    print_codes(root->left, str + "0", OutputFile);
    print_codes(root->right, str + "1", OutputFile);
}

void print_huffman(char *letters, int *freq, int n, ofstream &OutputFile)
{
    priority_queue<Node *, vector<Node *>, compare> h;
    for (int i = 0; i < n; i++)
    {
        h.push(new Node(letters[i], freq[i]));
    }
    while (h.size() > 1)
    {
        Node *l = h.top();
        h.pop();
        Node *r = h.top();
        h.pop();
        Node *node = new Node('$', l->freq + r->freq, l, r);
        h.push(node);
    }
    print_codes(h.top(), "", OutputFile);
}

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

int main()
{
    string text;
    ifstream InputFile("In0305.txt");
    getline(InputFile, text);
    InputFile.close();
    int len = text.length();
    char *letters = new char[len];
    int *freq = new int[len];
    int n = 7;
    ofstream OutputFile("Out0305.txt");
    frequency(letters, freq, text, OutputFile);
    print_huffman(letters, freq, n, OutputFile);
    OutputFile.close();
}
