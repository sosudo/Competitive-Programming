#include <bits/stdc++.h>
#define println(x) cout << x << "\n"
#define input(x, y) cin >> x >> y
#define sizeA(x) 3*x
#define sizeB(x) 2*x
using namespace std;
int main() {
	int a, b;
	input(a, b);
	int n = 0;
	while(a <= b) {
		a = sizeA(a);
		b = sizeB(b);
		n++;
	}
	println(n);
}
