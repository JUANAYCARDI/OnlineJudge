#include <iostream>
#include <vector>
#include <cstdio>
#include <climits>
#include <utility>
#include <map>
using namespace std;

int n;
vector<pair<int,int>> wAux(26, make_pair(INT_MAX, 0));
vector<vector<pair<int,int>>> w(101, wAux);
vector<int> nextAux(26, -1);
vector<vector<int>> nextA(26, nextAux);
map<char, int> iD;

void floydWarshall(vector<vector<pair<int,int>>> &w){

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			nextA[i][j] = j;
		}
	}
	
	for(int i = 0; i < n; i++){
		w[i][i] = make_pair(0, 0);
	}

	for(int k = 0; k < n; k++){
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(w[i][k].first != INT_MAX && w[k][j].first != INT_MAX && w[i][k].first + w[k][j].first < w[i][j].first){
					w[i][j].first = w[i][k].first + w[k][j].first;
					w[i][j].second = w[i][k].second + w[k][j].second;
					nextA[i][j] = nextA[i][k];				
				}
				else if(w[i][k].first != INT_MAX && w[k][j].first != INT_MAX && w[i][k].first + w[k][j].first == w[i][j].first){
					if(w[i][k].second + w[k][j].second < w[i][j].second){
						w[i][j].second = w[i][k].second + w[k][j].second;	
						nextA[i][j] = nextA[i][k];
					}	
				}
			}
		}
	}
}

int main(){
	
	iD['A'] = 0;
	iD['B'] = 1;
	iD['C'] = 2;
	iD['D'] = 3;
	iD['E'] = 4;
	iD['F'] = 5;
	iD['G'] = 6;
	iD['H'] = 7;
	iD['I'] = 8;
	iD['J'] = 9;
	iD['K'] = 10;
	iD['L'] = 11;
	iD['M'] = 12;
	iD['N'] = 13;
	iD['O'] = 14;
	iD['P'] = 15;
	iD['Q'] = 16;
	iD['R'] = 17;
	iD['S'] = 18;
	iD['T'] = 19;
	iD['U'] = 20;
	iD['V'] = 21;
	iD['W'] = 22;
	iD['X'] = 23;
	iD['Y'] = 24;
	iD['Z'] = 25;
	int i, j, p, d, q, planetAux, flag = 1;
	int p1, p2;
	char planet, e1, e2;
	scanf("%d %d", &n, &p);
	
	for(i = 0; i < p; i++){

		cin >> e1 >> e2 >> d;
		
		w[iD[e1]][iD[e2]] = make_pair(d, 0);
		w[iD[e2]][iD[e1]] = make_pair(d, 0);
			
	}
	scanf("%d", &q);
		
	floydWarshall(w);
		
	for(i = 0; i < q; i++){
		cin >> e1 >> e2;
		p1 = iD[e1];
		p2 = iD[e2];
		
		while(flag){
			planetAux = p1 + 65;
			planet = (char)planetAux;
			printf("%c ", planet);
			if(nextA[p1][p2] == p2){
				planetAux = p2 + 65;
				planet = (char)planetAux;
				printf("%c\n", planet);
				flag = 0;
			}
			else{
				p1 = nextA[p1][p2];
			}
		}
		flag = 1;
	}
	return 0;
}