#include <iostream>
#include <cstdlib>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

struct Node
{
    Node *next;
    Node *left;
    Node *right;
    char ch;
    int count;
};

void build_list(Node *&root, char *letters, int *freq, int n, ofstream &OutputFile)
{
    unsigned int i, x;
    char cx;
    Node *p;
    bool t;

    root = NULL;
    for (i = 0; i < n; i++)
    {
        p = root;
        while (p && (p->ch != letters[i]))
            p = p->next;
        if (!p)
        {
            p = new Node;
            p->next = root;
            p->left = NULL;
            p->right = NULL;
            p->ch = letters[i];
            p->count = freq[i];
            root = p;
        }
    }
    do
    {
        t = true;
        p = root;
        while (p->next)
        {
            if (p->count > p->next->count || ((p->count == p->next->count) && p->ch > p->next->ch))
            {
                cx = p->ch;
                p->ch = p->next->ch;
                p->next->ch = cx;
                x = p->count;
                p->count = p->next->count;
                p->next->count = x;
                t = false;
            }
            p = p->next;
        }
    } while (!t);
    int sum_of_count = 0.0;
    Node *count_list;
    count_list = new Node;
    count_list = root;
    for (i = 0; i < n; i++)
    {
        sum_of_count += count_list->count;
        count_list = count_list->next;
    }

    Node *display_list;
    display_list = new Node;
    display_list = root;
    for (i = 0; i < n; i++)
    {
        OutputFile << display_list->ch << " " << (float)display_list->count / (float)sum_of_count << ", ";
        display_list = display_list->next;
    }
}

void build_tree(Node *&root)
{
    Node *p, *r, *v1, *v2;

    while (true)
    {
        v1 = root;
        v2 = v1->next;
        if (!v2)
            break;

        root = v2->next;

        p = new Node;
        p->left = v1;
        p->right = v2;
        p->count = v1->count + v2->count;

        if (!root || (p->count < root->count))
        {
            p->next = root;
            root = p;
            continue;
        }

        r = root;
        while (r->next && (p->count >= r->next->count))
        {
            r = r->next;
        }

        p->next = r->next;
        r->next = p;
    }
}

void display_tree(Node *p, string b, ofstream &OutputFile)
{
    if (!p->left)
        OutputFile << p->ch << "=" << b << ", ";
    else
    {
        display_tree(p->left, b + "0", OutputFile);
        display_tree(p->right, b + "1", OutputFile);
    }
}

bool tree_code(char c, Node *p, string b, ofstream &OutputFile)
{
    if (!p->left)
    {
        if (c != p->ch)
            return false;
        else
        {
            OutputFile << b;
            return true;
        }
    }
    else
        return tree_code(c, p->left, b + "0", OutputFile) || tree_code(c, p->right, b + "1", OutputFile);
}

void huffman_code(Node *root, string s, ofstream &OutputFile)
{
    unsigned int i;

    for (i = 0; i < s.length(); i++)
        tree_code(s[i], root, "", OutputFile);
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

void tree_decode(Node *root, string code, int n, ofstream &OutputFile)
{
    Node *p;
    int i;
    p = root;
    for (i = 0; i < (int)code.length(); i++)
    {
        if (code[i] == '0')
            p = p->left;
        else
            p = p->right;
        if (!p->left)
        {
            OutputFile << p->ch;
            p = root;
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
    int n = sizeof(letters) / sizeof(letters[0]);
    ofstream OutputFile("Out0305.txt");
    frequency(letters, freq, text, OutputFile);
    Node *root;
    build_list(root, letters, freq, n + 1, OutputFile);

    ofstream OutputHuffFile("Huff.txt");
    // OutputHuffFile << n + 1 << endl;
    // Node *display_list;
    // display_list = new Node;
    // display_list = root;
    // cout << display_list->count;
    // for (int i = 0; i < n; i++)
    // {
    //     OutputHuffFile << display_list->ch << display_list->count << endl;
    //     display_list = display_list->next;
    // }

    build_tree(root);
    OutputFile << endl;
    display_tree(root, "", OutputFile);
    OutputFile << endl;
    OutputFile << "//////////////////////////////////" << endl;

    huffman_code(root, text, OutputHuffFile);
    OutputHuffFile.close();

    string code;
    ifstream InputHuffFile("Huff.txt");
    getline(InputHuffFile, code);
    InputHuffFile.close();
    tree_decode(root, code, n, OutputFile);
    OutputFile.close();
    return 0;
}
