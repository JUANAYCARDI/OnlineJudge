#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int n;
vector<vector<pair<int,int>>> ady(101);
vector<int> p(101);
vector<int> d(101);
vector<bool> inQueue(101);
vector<int> count(101);
bool ans = false;

void initialize(int s, int n){
	for(int i = 1; i < n + 1; i++){
		d[i] = INT_MAX;
		p[i] = -1;
		inQueue[i] = false;
		count[i] = 0;
	}
	d[s] = 0;
}

bool bellmanFordOpt(int s, int n){
	int i, j, u, v, weight;
	queue<int> q;
	
	
	initialize(s, n);

	q.push(s);
	inQueue[s] = true;

	while(!q.empty()){

		u = q.front();
		q.pop();
		inQueue[u] = false;

		for(i = 0; i < ady[u].size(); i++){
			v = ady[u][i].first;
			weight = ady[u][i].second;

			if(d[u] != INT_MAX && d[u] + weight < d[v]){

				d[v] = d[u] + weight;
				p[v] = u;
				if(v == 1 && d[v] < 0){
					ans = true;
					return true;
				}
				if(!inQueue[v]){
					q.push(v);
					inQueue[v] = true;
					count[v]++;

					if(count[v] > n){
						return false;
					}
				}
			}
		}
	}
	return true;
}

int main(){
	int n, b, i, u1, u2, t;
	vector<pair<int,int>> aux;
	scanf("%d %d", &n, &b);
	while(n != 0 && b != 0){
		ans = false;
		for(i = 0; i < b; i++){
			scanf("%d %d %d", &u1, &u2, &t);
			ady[u1].push_back(make_pair(u2, t));
			ady[u2].push_back(make_pair(u1, 0 - t));
		}
		bellmanFordOpt(1, n);

		if(ans){
			printf("Y\n");
		}
		else{
			printf("N\n");
		}
		for(i = 1; i < n + 1; i++){
			ady[i] = aux;
		}
		scanf("%d %d", &n, &b);
		}
	return 0;
}