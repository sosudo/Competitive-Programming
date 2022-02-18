#include <iostream>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
#define calc(k, n, w) ((k*w*(w+1))/2)-n
using namespace std;
int main() {
	int k, n, w;
	input(k);
	input(n);
	input(w);
	print(max(calc(k, n, w), 0));
}
