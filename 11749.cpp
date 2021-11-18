#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <cstdio>
#include <algorithm>
using namespace std;

void ccDFSAux(int v, vector<vector<int>> &ady, vector<bool> &visited, int &maxC, map<pair<int,int>,int> &ppa, int &cities){
  	int w;
  	visited[v] = true;
  	cities += 1;
  	for(int i = 0; i < ady[v].size(); i++){
    	w = ady[v][i];
    	if(!visited[w] && ppa[{min(v, w), max(v, w)}] == maxC){
      		ccDFSAux(w, ady, visited, maxC, ppa, cities);
    	}
  	}
}

int ccDFS(int &n, vector<vector<int>> &ady, vector<bool> &visited, int &maxC, map<pair<int,int>,int> &ppa){
  	int i, maxCities = -1, cities = 0;
  
  	for(i = 0; i < n; i++){
    	visited[i] = false;
  	}

  	for(i = 0; i < n; i++){
    	if(!visited[i]){
    		cities = 0;
      		ccDFSAux(i, ady, visited, maxC, ppa, cities);
      		if(cities > maxCities){
      			maxCities = cities;
      		}
      	}
    }
    return maxCities;
}


int main(){
	int n, a, b, c, maxC;
	long int m, i;
	vector<int> aux;
	vector<vector<int>> ady(500, aux);
	vector<bool> visited(500, false);
	map<pair<int,int>,int> ppa;
	map<pair<int,int>,int>::iterator it;
	scanf("%d %ld", &n, &m);
	while(n != 0){
		for(i = 0; i < m; i++){
			scanf("%d %d %d", &a, &b, &c);
			
			it = ppa.find({min(a - 1, b - 1), max(a - 1, b - 1)});

			if(it == ppa.end()){
				ppa[make_pair(min(a - 1, b - 1), max(a - 1, b - 1))] = c;
				ady[a - 1].push_back(b - 1);
				ady[b - 1].push_back(a - 1);
				if(i == 0){
					maxC = c;
				}
				else{
					if(c > maxC){
						maxC = c;
					}
				}		
			}
			else{
				if(c > ppa[{min(a - 1, b - 1), max(a - 1, b - 1)}]){
					ppa[{min(a - 1, b - 1), max(a - 1, b - 1)}] = c;
					if(c > maxC){
						maxC = c;
					}
				}
			}
		}

		int result = ccDFS(n, ady, visited, maxC, ppa);
		printf("%d\n", result);
		ppa.clear();
		for(int i = 0; i < n; i++){
			ady[i] = aux;
		}

		scanf("%d %ld", &n, &m);
	}
	return 0;
}
