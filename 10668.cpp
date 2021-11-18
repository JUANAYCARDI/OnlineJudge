#include <iostream>
#include <stdio.h>
#include <math.h>
#include <cmath>

using namespace std;

double radius(int l, double lim){
	double r;
	r = (lim/2) + ((pow(l,2))/(8*lim));
	return r;
}

double angle(int l, double r){
	double a;
	a = 2*(asin(l/(2*r)));
	return a;
}

int main(){
	int l, n;
	double c, eps = 0.0001;
	scanf("%d %d %lf", &l, &n, &c);
	while(l > -1 and n > -1 and c > -1){
		double newL = (1 + n * c) * l;
		double r, a, lowI = 0, highI = l/2, midI = 0;
		r = radius(l, lowI);
		a = angle(l, r);
		double low, mid, high;
		low = r * a;
		r = radius(l, highI);
		a = angle(l, r);
		high = r * a;
		while(abs(highI - lowI) > eps and n != 0 and c != 0){
			midI = (lowI + highI)/2;
			r = radius(l, midI);
			a = angle(l, r);
			mid = r * a;
			if(mid <= newL){
				lowI = midI;
				low = mid;
			}
			else{
				highI = midI;
				high = mid;
			}
		}
		printf("%.3lf\n", midI);
		scanf("%d %d %lf", &l, &n, &c);
	}
	
	return 0;
}