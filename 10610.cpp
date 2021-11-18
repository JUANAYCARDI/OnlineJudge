#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <map>
#include <math.h>
#include <queue>
#include <algorithm> 

using namespace std;

int bfsAux(int n, vector<vector<int>> &ady, vector<int> &v){
  int u, w, i;
  queue<int> queue;
  v[n] = 1;
  queue.push(n);
  int min = -1, count = 0, count2 = queue.size(), depth = 0;
  while(!queue.empty()){
    u = queue.front();
    queue.pop();
    if(count2-- == 0){
    	count += 1;
    	count2 = queue.size();
    }
    for(i = 0; i < ady[u].size(); i++){    
      w = ady[u][i];
      if(!v[w]){
      	if(w == 1){
      		min = count;
      		return min;    		
      	}
      	else{
      		v[w] = 1;
			queue.push(w);
      	}     	
      }
    }   
  }
  return min;
}

int bfs(vector<vector<int>> &ady, vector<int> &v){
    return bfsAux(0, ady, v);
}

double distanceLimit(double x1, double y1, double x2, double y2, double limit){ 
 	double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
	return distance <= limit;                                                      
} 

int main(){
	int v, m, i, j;
	double x, y;
	string line;
	scanf("%d %d\n", &v, &m);
	vector<vector<int>> ady(1002);
	while(v != 0 and m != 0){
		map<int, pair<double, double>> id;
		int pairID = 0;
		getline(cin, line);
		double maxDistance;
		maxDistance = (m*60)*v;
		vector<int> aux;
		while(line != ""){
			string::size_type s;
			x = stod(line, &s);
			y = stod(line.substr(s));
			id[pairID++] = {x,y};
			getline(cin, line);
		}
		vector<int> v2(id.size(), 0);
		for(i = 0; i < id.size(); i++){
			for(j = i + 1; j < id.size(); j++){
				if(distanceLimit(id[i].first, id[i].second, id[j].first, id[j].second, maxDistance)){
					ady[i].push_back(j);
					ady[j].push_back(i);									
				}
				
			}
		}
		vector<int> visited(id.size(), 0);
		int result = bfs(ady, visited);
		scanf("%d %d\n", &v, &m);
		if(result != -1){
			printf("Yes, visiting %d other holes.\n", result);
		}
		else{
			printf("No.\n");
		}
		fill(ady.begin(), ady.begin() + id.size(), aux);
	}


	return 0;
}