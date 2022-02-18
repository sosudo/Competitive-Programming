#include <iostream>
#include <algorithm>
#define print(a, b, c) cout << a << " " << b <<  " " << c << "\n"
#define input(a, b, c, d, e, f, g) cin >> a >> b >> c >> d >> e >> f >> g
#define s(x) sort(x, x + sizeof(x)/sizeof(x[0]))
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int x[7] = {0};
	input(x[0], x[1], x[2], x[3], x[4], x[5], x[6]);
	s(x);
	print(x[0], x[1], x[6]-x[1]-x[0]);
}
