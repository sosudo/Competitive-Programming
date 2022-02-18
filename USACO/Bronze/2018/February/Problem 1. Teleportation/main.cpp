#include <iostream>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
#define dist(a, b) abs(b-a)
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("teleport.in", "r", stdin);
	freopen("teleport.out", "w", stdout);
	int a, b, x, y;
	input(a);
	input(b);
	input(x);
	input(y);
	print(min(dist(a, b), min(dist(a, x), dist(a, y)) + min(dist(x, b), dist(y, b))));
}
