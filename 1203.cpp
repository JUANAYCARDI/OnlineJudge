#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <utility>

using namespace std;

int main(){
	int qNum, pNum, k, i;
	string registro = "-";
	priority_queue<pair<int , int> , vector<pair<int , int>>, greater<pair<int , int>>> numeros;
	map<int , int> registros;
	while(registro != "#"){
		cin >> registro;
		if(registro != "#"){
			cin >> qNum;
			cin >> pNum;
			registros[qNum] = pNum;
			numeros.push(make_pair(pNum , qNum));
		}
	}
	cin >> k;
	while(k--){
		cout << numeros.top().second << endl;
		numeros.push(make_pair(numeros.top().first + registros[numeros.top().second] , numeros.top().second));
		numeros.pop();
	}
	return 0;
}