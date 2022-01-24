#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

#define INF 9999999

bool bellman_ford(int **weights_graph, int distance[], int n, int source = 1)
{
    distance[source] = 0;

    for (int i = source; i < n + 1; i++)
    {
        for (int j = source; j < n + 1; j++)
            for (int k = source; k < n + 1; k++)
                distance[k] = min(distance[k], distance[j] + weights_graph[j][k]);
    }

    for (int i = source; i < n + 1; i++)
        for (int j = source; j < n + 1; j++)
            if (distance[j] > distance[i] + weights_graph[i][j])
                return false;
    return true;
}

int min_distance(int distance[], bool visited[], int n)
{
    int min = INF, min_index = -1;
    for (int i = 0; i < n + 1; i++)
    {
        if (visited[i] == false && distance[i] <= min)
        {
            min = distance[i];
            min_index = i;
        }
    }
    return min_index;
}

void dijkstra(int **weights_graph, int *distance, int n, int source = 1)
{
    bool visited[n];
    for (int i = 0; i < n + 1; i++)
    {
        distance[i] = INF;
        visited[i] = false;
    }

    distance[source] = 0;

    for (int i = 0; i < n; i++)
    {
        int min_v_d_id = min_distance(distance, visited, n);
        visited[min_v_d_id] = true;

        for (int j = 0; j < n + 1; j++)
        {
            if (!visited[j] && distance[min_v_d_id] != INF && distance[min_v_d_id] + weights_graph[min_v_d_id][j] < distance[j])
            {
                distance[j] = distance[min_v_d_id] + weights_graph[min_v_d_id][j];
            }
        }
    }
}

int main()
{
    int n;
    ifstream InputFile("In0401.txt");
    InputFile >> n;
    int **weights_graph = new int *[n + 1];
    int *distance = new int[n + 1];
    int *dijkstra_distance = new int[n + 1];
    for (int i = 1; i < n + 1; i++)
        distance[i] = INF;
    for (int i = 0; i < n + 1; i++)
    {
        weights_graph[i] = new int[n + 1];
    }
    for (int i = 0; i < n + 1; i++)
    {
        weights_graph[0][i] = 0;
    }
    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 0; j < n + 1; j++)
        {
            weights_graph[i][j] = INF;
            if (i == j)
            {
                weights_graph[i][j] = 0;
            }
        }
    }
    string line;
    getline(InputFile, line);
    int i = 1;
    while (getline(InputFile, line))
    {
        istringstream ss(line);
        int num1, num2;
        while (ss >> num1 >> num2)
        {
            weights_graph[i][num1] = num2;
        }
        i++;
    }

    ofstream OutputFile("Out0401.txt");
    bellman_ford(weights_graph, distance, n, 0);

    for (int i = 0; i < n + 1; i++)
        OutputFile << distance[i] << " ";
    OutputFile << endl;

    for (int i = 0; i < n + 1; i++)
    {

        for (int j = 0; j < n + 1; j++)
        {
            if (weights_graph[i][j] != INF)
            {
                weights_graph[i][j] = weights_graph[i][j] + distance[i] - distance[j];
            }
        }
    }

    for (int i = 0; i < n + 1; i++)
    {
        OutputFile << "[" << i << "]\t";
        for (int j = 1; j < n + 1; j++)
        {
            if (weights_graph[i][j] != INF && j != i)
            {
                OutputFile << j << "(" << weights_graph[i][j] << ") ";
            }
        }
        OutputFile << endl;
    }

    for (int i = 1; i < n + 1; i++)
    {
        dijkstra(weights_graph, dijkstra_distance, n, i);
        OutputFile << "Delta^[" << i << "][";
        for (int j = 1; j < n + 1; j++)
        {
            if (dijkstra_distance[j] != INF)
                OutputFile << dijkstra_distance[j] << " ";
            else
                OutputFile << "∞ ";
        }
        OutputFile << "],D[" << i << "][";
        for (int j = 1; j < n + 1; j++)
        {
            if (dijkstra_distance[j] != INF)
                OutputFile << dijkstra_distance[j] + distance[j] - distance[i] << " ";
            else
                OutputFile << "∞ ";
        }
        OutputFile << "]\n";
    }
    OutputFile.close();
    return 0;
}