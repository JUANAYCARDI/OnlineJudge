#include <vector>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;


int main(){
    int n, m, i;
    scanf("%d %d", &n, &m);
    vector<vector<int>> ady(1000002);
    vector<int> inc(1000002, 0);
    vector<int> aux;
    while(n != 0){
        
        int a, b, u, v, vis = 0;
        
        for(i = 0; i < m; i++){
            scanf("%d %d", &a, &b);
            ady[a - 1].push_back(b - 1);
            inc[b-1]++;
        }
        queue<int> queue;
        vector<int> topo;
        for(i = 0; i < n; ++i){
            if(inc[i] == 0){
                queue.push(i);
            }
        }

        while(!queue.empty()){
            v = queue.front();
            queue.pop();
            topo.push_back(v);

            for(i = 0; i < ady[v].size(); i++){
                u = ady[v][i];
                inc[u]--;
                if(inc[u] == 0){
                    queue.push(u);
                }
            }

            vis++;
        }

        if(vis != n){
            printf("IMPOSSIBLE\n");
        }
        else{
            for(i = 0; i < n; i++){
                printf("%d\n", topo[i] + 1);
            }
        }      
        fill(ady.begin(), ady.begin() + n, aux);
        fill(inc.begin(), inc.begin() + n, 0);
        scanf("%d %d", &n, &m);

    }
    
    return 0;
}