#include <iostream>
#include <list>
#include <string>
using namespace std;

int main(){
    string broken;
	while(cin >> broken){
		list<char> fixed;
		list<char>::iterator it = fixed.end();
		for(int i = 0; i < broken.size(); i++){
			if(broken[i] == '['){
				it = fixed.begin();
			}
			else if(broken[i] == ']'){
				it = fixed.end();
			}
			else{
				fixed.insert(it,broken[i]);
			}
		}
		for(it = fixed.begin(); it != fixed.end(); it++){
			printf("%c", *it);
		}
		printf("\n");;
	}			
	return 0;
}		