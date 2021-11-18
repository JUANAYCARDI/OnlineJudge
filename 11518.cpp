#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm> 
using namespace std;

int dfsAux(vector<int> &v, vector<vector<int>> &l ,int p, int acum){			
	acum += 1;
	v[p] = 1;
	for(int i = 0; i < l[p].size(); i++){
		if(v[l[p][i]-1] == 0){
			acum += dfsAux(v, l, l[p][i]-1, 0);								
		}
	}
	return acum;
}

int dfs(vector<int> &v, vector<vector<int>> &l, int p){
	int count = 0;	
	count += 1;
	v[p] = 1;
	for(int i = 0; i < l[p].size(); i++){
		if(v[l[p][i]-1] == 0){
			count += dfsAux(v, l, l[p][i]-1, 0);	
		}	
	}
	return count;
}


int main(){
	int cases;
	scanf("%d", &cases);
	while(cases--){
		int n, m, l, i, x, y;
		scanf("%d %d %d", &n, &m, &l);
		vector<int> visited(n,0);
		vector<vector<int>> ady(n);
		vector<int>::iterator it;
		for(i = 0; i < m; i++){
			scanf("%d %d", &x, &y);
			it = find(ady[x-1].begin(), ady[x-1].end(), y);
			if(it == ady[x-1].end()){
				ady[x-1].push_back(y);
			}	
		}

		int push;
		int total = 0;
		for(i = 0; i < l; i++){
			scanf("%d", &push);
			if(visited[push-1] == 0){
				total += dfs(visited,ady,push-1);		
			}			
		}
		printf("%d\n", total);
	}
	return 0;
}