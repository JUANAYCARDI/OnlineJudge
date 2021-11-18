#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <climits>
using namespace std;

int n;
vector<int> wAux(101, INT_MAX);
vector<vector<int>> w1(101, wAux);
vector<vector<int>> w2(101, wAux);

void floydWarshall(vector<vector<int>> &w1, vector<vector<int>> &w2){
	
	for(int i = 1; i < n + 1; i++){
		w1[i][i] = 0;
		w2[i][i] = 0;
	}

	for(int k = 1; k < n + 1; k++){
		for(int i = 1; i < n + 1; i++){
			for(int j = 1; j < n + 1; j++){
				if(w1[i][k] != INT_MAX && w1[k][j] != INT_MAX && w1[i][k] + w1[k][j] < w1[i][j]){
					w1[i][j] = w1[i][k] + w1[k][j];
				}
				if(w2[i][k] != INT_MAX && w2[k][j] != INT_MAX && w2[i][k] + w2[k][j] < w2[i][j]){
					w2[i][j] = w2[i][k] + w2[k][j];
				}
			}
		}
	}
}

int main(){
	int i, j, node, count, a, b, flag;
	string line;
	scanf("%d\n", &n);
	while(n != 0){
		flag = 0;
		for(i = 0; i < n; i++){
			getline(cin, line);
			stringstream ss(line);		
			count = 1;
    		for(j = 0; ss >> j;){
    			if(count == 1){
    				node = j;
    				count++;
    			}
    			else{
    				w1[node][j] = 1;
    			}
    		}
		}
		for(i = 0; i < n; i++){
			getline(cin, line);
			stringstream ss(line);		
			count = 1;
    		for(j = 0; ss >> j;){
    			if(count == 1){
    				node = j;
    				count++;
    			}
    			else{
    				w2[node][j] = 1;
    			}
    		}
		}
		scanf("%d %d", &a, &b);
		floydWarshall(w1,w2);
		
		for(i = 1; i < n + 1; i++){
			for(j = 1; j < n + 1; j++){
				if(w2[i][j] > ((a * w1[i][j]) + b)){
					printf("No\n");
					flag = 1;
					break;
				}
			}
			if(flag){
				break;
			}
		}
		if(!flag){
			printf("Yes\n");
		}
		for(i = 1; i < n + 1; i++){
			w1[i] = wAux;
			w2[i] = wAux;
		}
		scanf("%d\n", &n);
	}	
	return 0;
}