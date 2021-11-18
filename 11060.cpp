#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;


int main(){
    int n, m, i, cases = 0;
    while(scanf("%d", &n) != EOF){
        cases++;
        vector<vector<int>> ady(n);
        vector<int> inc(n, 0);
        map<string, int> iD; 
        map<int, string> iD2;
        string beverage;
        int u, v;
        string a, b;
        for(i = 0; i < n; i++){
            cin >> beverage;
            iD[beverage] = i;
            iD2[i] = beverage;
        }
        scanf("%d", &m);
        for(i = 0; i < m; i++){
            cin >> a >> b;
            ady[iD[a]].push_back(iD[b]);
            inc[iD[b]]++;
        }
        priority_queue<int, vector<int>, greater<int>> queue;
        vector<int> topo;
        for(i = 0; i < n; ++i){
            if(inc[i] == 0){
                queue.push(i);
            }
        } 

        while(!queue.empty()){
            v = queue.top();
            queue.pop();
            topo.push_back(v);

            for(i = 0; i < ady[v].size(); i++){
                u = ady[v][i];
                inc[u]--;
                if(inc[u] == 0){
                    queue.push(u);
                }
            }
        }

        cout << "Case #" << cases << ": Dilbert should drink beverages in this order: ";
        for(i = 0; i < n - 1; i++){
            cout << iD2[topo[i]] << " ";
        }
        cout << iD2[topo[i]] << '.' << endl;
        printf("\n"); 
        
    }
    
    return 0;
}