#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int t;
struct Compare{
	bool operator()(pair<int,int> &a, pair<int,int> &b){
		if(a.second > b.second){
			return true;
		}
		else if(a.second < b.second){
			return false;
		}
		else{
			if(a.first < b.first){
				return true;
			}
			else{
				return false;
			}
		}
	}
};

void apAux(int v, vector<vector<int>> &ady, vector<int> &visited, vector<pair<int,int>> &apNodes, vector<int> &father, vector<int> &low){
  	int w, numHijos = 0;
  	visited[v] = low[v] = ++t;
  	for(int i = 0; i < ady[v].size(); i++){
    	w = ady[v][i];
    	if(visited[w] == -1){
      		numHijos++;
      		father[w] = v;
      		apAux(w, ady, visited, apNodes, father, low);
      		low[v] = min(low[v], low[w]);
      		if(father[v] != -1 && low[w] >= visited[v]){
				apNodes[v].second += 1;
      		}
    	}
    	else if(w != father[v]){
      		low[v] = min(low[v], visited[w]);
    	}
  	}
  	if(father[v] == -1 && numHijos > 1){
    	apNodes[v].second += numHijos - 1;
  	}
}

void ap(int n, vector<vector<int>> &ady, vector<int> &visited, vector<pair<int,int>> &apNodes, vector<int> &father, vector<int> &low){
  	int i;

  	for(i = 0; i < n; i++){
    	if(visited[i] == -1){
      		apAux(i, ady, visited, apNodes, father, low);
    	}
  	}
}

int main(){
	vector<int> aux;
	vector<vector<int>> ady(10000, aux);
	vector<int> visited(10000, -1);
	vector<pair<int,int>> apNodes(10000);
	for(int i = 0; i < apNodes.size(); ++i){
		apNodes[i] = make_pair(i, 1);
	}
	vector<int> father(10000, -1);
	vector<int> low(10000, -1);
	int n, m, a, b;
	scanf("%d %d", &n, &m);
	scanf("%d %d", &a, &b);
	while(n != 0 && m != 0){
		while(a != -1 && b != -1){
			t = 1;
			ady[a].push_back(b);
			ady[b].push_back(a);
			scanf("%d %d", &a, &b);
		}
		ap(n, ady, visited, apNodes, father, low);

		sort(apNodes.begin(), apNodes.begin() + n, Compare());

		for (int i = 0; i < m; ++i){
			printf("%d %d\n", apNodes[i].first, apNodes[i].second);
		}
		printf("\n");

		fill(ady.begin(), ady.begin() + n, aux);
		fill(visited.begin(), visited.begin() + n, -1);
		for(int i = 0; i < n; ++i){
			apNodes[i] = make_pair(i, 1);
		}
		fill(father.begin(), father.begin() + n, -1);
		fill(low.begin(), low.begin() + n, -1);
		scanf("%d %d", &n, &m);
		scanf("%d %d", &a, &b);
	}
	return 0;
}