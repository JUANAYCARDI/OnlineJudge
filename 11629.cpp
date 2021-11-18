#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <math.h>

using namespace std;

int main(){
	int parties, guesses, i, j, k, count = 1;
	float value, total;
	string party, guess, aux;
	map<string, float> p;

	cin >> parties >> guesses;
	
	for(i = 0; i < parties; i++){
		cin >> party >> value;
		p[party] = value;
	}

	cin.ignore();

	for(i = 0; i < guesses; i++){
		getline(cin, guess);
		k = 0;
		total = 0;
		for(j = 0; j < guess.size(); j++){
			if(guess[j] == ' '){
				aux = guess.substr(k, j-k);
				total += p[aux];
				j += 1;
				k = j + 2;
				if(guess[j] != '+'){

					if(guess[j] == '<'){

						if(guess[j+1] == '='){
							
							if(roundf(total * 10) / 10 <= stoi(guess.substr(j+3, guess.size() - j+3))){
								
								cout << "Guess #" << count++ << " was correct." << endl;
								j = guess.size();
							}
							else{
								cout << "Guess #" << count++ << " was incorrect." << endl;
								j = guess.size();
							}
						}
						else{
							
							if(roundf(total * 10) / 10 < stoi(guess.substr(j+2, guess.size() - j+2))){
								
								cout << "Guess #" << count++ << " was correct." << endl;
								j = guess.size();
							}
							else{
								cout << "Guess #" << count++ << " was incorrect." << endl;
								j = guess.size();
							}
						}
					}
					else if(guess[j] == '>'){
						if(guess[j+1] == '='){
							
							if(roundf(total * 10) / 10 >= stoi(guess.substr(j+3, guess.size() - j+3))){
								
								cout << "Guess #" << count++ << " was correct." << endl;
								j = guess.size();
							}
							else{
								cout << "Guess #" << count++ << " was incorrect." << endl;
								j = guess.size();
							}
						}
						else{
							
							if(roundf(total * 10) / 10 > stoi(guess.substr(j+2, guess.size() - j+2))){
								
								cout << "Guess #" << count++ << " was correct." << endl;
								j = guess.size();
							}
							else{
								cout << "Guess #" << count++ << " was incorrect." << endl;
								j = guess.size();
							}
						}
					}
					else{
						
						if(roundf(total * 10) / 10 == stoi(guess.substr(j+2, guess.size() - j+2))){
							
							cout << "Guess #" << count++ << " was correct." << endl;
							j = guess.size();
						}
						else{
							cout << "Guess #" << count++ << " was incorrect." << endl;
							j = guess.size();
						}
					}
				}
				else{
					j += 1;
				}
			}

		}
	}
	return 0;
}