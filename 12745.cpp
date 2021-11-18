#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <math.h>
#include <algorithm>
#include <utility>
#include <set>
using namespace std;

int numSCC, t;
bool answer = true;

void tarjanAux(int v, vector<vector<int>> &ady, vector<int> &visited, vector<int> &sccInd, vector<bool> &inStack, stack<int> &st, vector<vector<int>> &sccNodes, int n){
	int w, i;
	visited[v] = sccInd[v] = t++;
	st.push(v);
	inStack[v] = true;
	
	for(i = 0; i < ady[v].size(); i++){
		w = ady[v][i];
		if(visited[w] == -1){
			tarjanAux(w, ady, visited, sccInd, inStack, st, sccNodes, n);
			sccInd[v] = min(sccInd[v], sccInd[w]);
		}
		else if(inStack[w]){
			sccInd[v] = min(sccInd[v], visited[w]);
		}
	}
	vector<int>::iterator it;
	if(sccInd[v] == visited[v]){
		
		sccNodes.push_back(vector<int>());
		numSCC++;
		int aux;
		if(v > n){
			aux = (v - n) * -1;
		}
		else{
			aux = v;
		}		
		while(st.top() != v){
			
			inStack[st.top()] = false;
			if(st.top() > n){
				it = find(sccNodes[numSCC - 1].begin(), sccNodes[numSCC - 1].end(), st.top() - n);
				if(it != sccNodes[numSCC - 1].end()){
					answer = false;
				}
				sccNodes[numSCC - 1].push_back(st.top() - n);
			}
			else{
				it = find(sccNodes[numSCC - 1].begin(), sccNodes[numSCC - 1].end(), st.top());
				if(it != sccNodes[numSCC - 1].end()){
					answer = false;
				}
				sccNodes[numSCC - 1].push_back(st.top());
			}			
			st.pop();
		}

		inStack[st.top()] = false;
		if(st.top() > n){
			it = find(sccNodes[numSCC - 1].begin(), sccNodes[numSCC - 1].end(), st.top() - n);
			if(it != sccNodes[numSCC - 1].end()){
				answer = false;
			}
			sccNodes[numSCC - 1].push_back(st.top() - n);
		}
		else{
			it = find(sccNodes[numSCC - 1].begin(), sccNodes[numSCC - 1].end(), st.top());
			if(it != sccNodes[numSCC - 1].end()){
				answer = false;
			}
			sccNodes[numSCC - 1].push_back(st.top());
		}
		st.pop();
	}
}


void tarjan(int n, vector<vector<int>> &ady, vector<int> &visited, vector<int> &sccInd, vector<bool> &inStack, stack<int> &st, vector<vector<int>> &sccNodes){
	int i;

	for(i = 1; i < n; i++){
		sccInd[i] = visited[i] = -1;
		inStack[i] = false;
	}

	for(i = 1; i < n; i++){
		if(visited[i] == -1){
			tarjanAux(i, ady, visited, sccInd, inStack, st, sccNodes, n/2);
		}
	}
}

int main(){
	int cases, i, j, count = 1;
	vector<int> aux;
	vector<vector<int>> ady(200002);
	vector<int> visited(200002, -1);
	vector<int> sccInd(200002, -1);
	vector<bool> inStack(200002, false);
	set<pair<int, int>> blackSet;
	set<pair<int, int>>::iterator ite;
	stack<int> st;
	vector<vector<int>> sccNodes;
	scanf("%d", &cases);
	
	while(cases--){
		t = 1;
		numSCC = 0;
		answer = true;
		int n, m, w1, w2;
		scanf("%d %d", &n, &m);		
		
		for(i = 0; i < m; i++){
			scanf("%d %d", &w1, &w2);
			blackSet.insert(make_pair(w1,w2));
			blackSet.insert(make_pair(w2,w1));
			if(w1 < 0){
				if(w2 < 0){
					ite = blackSet.find(make_pair(w1, abs(w2)));					
					if(ite == blackSet.end()){
						ady[abs(w1) + n].push_back(abs(w2));
					}
					ite = blackSet.find(make_pair(abs(w1), w2));					
					if(ite == blackSet.end()){
						ady[abs(w1)].push_back(abs(w2) + n);	
					}						
				}
				else{
					ite = blackSet.find(make_pair(w1, 0 - w2));
					if(ite == blackSet.end()){
						ady[abs(w1) + n].push_back(w2 + n);
					}
					ite = blackSet.find(make_pair(abs(w1), w2));
					if(ite == blackSet.end()){
						ady[abs(w1)].push_back(w2);
					}
				}
			}
			else{
				if(w2 < 0){					
					ite = blackSet.find(make_pair(w1, abs(w2)));					
					if(ite == blackSet.end()){
						ady[w1].push_back(abs(w2));	
					}
					ite = blackSet.find(make_pair(0 - w1, w2));					
					if(ite == blackSet.end()){
						ady[w1 + n].push_back(abs(w2) + n);
					}					
				}
				else{
					ite = blackSet.find(make_pair(w1, 0 - w2));					
					if(ite == blackSet.end()){
						ady[w1].push_back(w2 + n);
					}
					ite = blackSet.find(make_pair(0 - w1, w2));					
					if(ite == blackSet.end()){
						ady[w1 + n].push_back(w2);
					}					
				}
			}
		}
		
		tarjan(n*2, ady, visited, sccInd, inStack, st, sccNodes);
				
		printf("Case %d: ", count);
		if(answer){
			printf("Yes\n");
		}
		else{
			printf("No\n");
		}

		for(i = 0; i < n * 2; i++){
			ady[i] = aux;
			visited[i] = -1;
			sccInd[i] = -1;
			inStack[i] = false;
		}
		blackSet.clear();
		sccNodes.clear();
		count += 1;
	}
	return 0;
}