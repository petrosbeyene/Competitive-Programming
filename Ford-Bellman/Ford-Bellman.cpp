#include <iostream>
#include <vector>

using namespace std;

class Graph {
public:
    vector<vector<int>> graphList;

    void addEdge(int u, int v, int w) {
        graphList.push_back({u, v, w});
    }
};

vector<int> bellmanFord() {
    int n, e;
    cin >> n >> e;
    Graph graph;
    for (int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.addEdge(u, v, w);
    }

    vector<int> distances(n, 30000);
    distances[0] = 0;
    for (int i = 0; i < n - 1; i++) {
        for (auto edge : graph.graphList) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (distances[u - 1] != 30000 && distances[u - 1] + w < distances[v - 1]) {
                distances[v - 1] = distances[u - 1] + w;
            }
        }
    }

    return distances;
}

int main() {
    vector<int> result = bellmanFord();
    for (int distance : result) {
        cout << distance << " ";
    }
    cout << endl;
    return 0;
}
