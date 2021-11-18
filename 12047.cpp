#include <iostream>
#include <climits>
#include <vector>
#include <queue>
#include <cstdio>
#include <algorithm>
using namespace std;

int n, result = -1;
vector<vector<pair<int,int>>> ady(10001);
vector<vector<pair<int,int>>> ady2(10001);
vector<int> p(10001);
vector<int> d(10001);
vector<int> p2(10001);
vector<int> d2(10001);

void initialize(int s, vector<int> &pr, vector<int> &di){
	for(int i = 1; i < n + 1; i++){
		di[i] = INT_MAX;
		pr[i] = -1;
	}

	di[s] = 0;
}

void dijkstra(int s, vector<vector<pair<int,int>>> &adyL, vector<int> &pr, vector<int> &di){
	int i, j, k, u, v, weight, cost;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> q;
	initialize(s, pr, di);
	q.push(make_pair(0,s));

	while(!q.empty()){
		cost = q.top().first;
		u = q.top().second;
		q.pop();

		if(cost == di[u]){
			for(j = 0; j < adyL[u].size(); j++){
				v = adyL[u][j].first;
				weight = adyL[u][j].second;
				if(di[u] != INT_MAX && di[u] + weight < di[v]){
					di[v] = di[u] + weight;
					pr[v] = u;					
					q.push(make_pair(di[v], v));
				}
			}
		}
	}
}

int main(){
	vector<pair<int,int>> aux;
	priority_queue<pair<int, pair<int,int>>, vector<pair<int, pair<int,int>>>> edges;
	int cases, m, s, t, pa, u, v, c, i, sum1, sum2;
	scanf("%d", &cases);
	while(cases--){
		scanf("%d %d %d %d %d", &n, &m, &s, &t, &pa);
		result = -1;
		for(i = 0; i < m; i++){
			scanf("%d %d %d", &u, &v, &c);
			ady[u].push_back(make_pair(v, c));
			ady2[v].push_back(make_pair(u, c));
			edges.push(make_pair(c, make_pair(u, v)));
		}
		
		dijkstra(s, ady, p, d);
		dijkstra(t, ady2, p2, d2);
		while(!edges.empty()){	
			sum1 = d[edges.top().second.first];
			sum2 = d2[edges.top().second.second];
			if(sum1 + sum2 + edges.top().first <= pa && sum1 != INT_MAX && sum2 != INT_MAX){
				result = edges.top().first;
				break;
			}
			edges.pop();
		}
	
		while(!edges.empty()){
			edges.pop();
		}
		for(i = 1; i < n + 1; i++){
			ady[i] = aux;
			ady2[i] = aux;
		}
		if(result <= pa){
			printf("%d\n", result);
		}
		else{
			printf("-1\n");
		}		
	}
	return 0;
}