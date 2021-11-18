#include <cstdio>
#include <vector>
#include <list>
using namespace std;

void kosarajuAux(int v, vector<vector<int>> &ady, list<int> &ord, vector<int> &visited){
	if(visited[v] == 0){
		visited[v] = 1;

		for(int i = 0; i < ady[v].size(); i++){
			kosarajuAux(ady[v][i], ady, ord, visited);
		}
		ord.push_front(v);
	}	
}

int kosaraju(int nodes, vector<int> &visited, vector<vector<int>> &ady, list<int> &ord){
	int i, count, total = 0;

	for(i = 0; i < nodes; i++){
		kosarajuAux(i, ady, ord, visited);
	}
	for(i = 0; i < nodes; i++){
		visited[i] = 0;
	}
	for(list<int>::iterator it = ord.begin(); it != ord.end(); it++){
		if(visited[*it] == 0){
			kosarajuAux(*it, ady, ord, visited);
			total += 1;
		}		
	}
	return total;
}

int main(){
	int cases;
	vector<int> visited(100000,0);
	vector<vector<int>> ady(100000);
	vector<int> aux;
	scanf("%d", &cases);
	while(cases--){
		list<int> ord;
		int i, nodes, edges, node1, node2;
		scanf("%d %d", &nodes, &edges);
		for(i = 0; i < edges; i++){
			scanf("%d %d", &node1, &node2);
			ady[node1-1].push_back(node2-1);
		}
		int result = kosaraju(nodes, visited, ady, ord);
		printf("%d\n", result);
		for(i = 0; i < nodes; i++){
			ady[i] = aux;
			visited[i] = 0;
		}
	}
	return 0;
}