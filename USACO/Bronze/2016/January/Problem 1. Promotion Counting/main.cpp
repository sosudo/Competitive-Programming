#include <iostream>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("promote.in", "r", stdin);
	freopen("promote.out", "w", stdout);
	int b1, b2, s1, s2, g1, g2, p1, p2, a1, a2, a3;
	input(b1);
	input(b2);
	input(s1);
	input(s2);
	input(g1);
	input(g2);
	input(p1);
	input(p2);
	int start = b1+s1+g1+p1;
	int end = b2+s2+g2+p2;
	int diff = end-start;
	b1 += diff;
	int bronze = b1-b2;
	print(bronze);
	s1 += bronze;
	int silver = s1-s2;
	print(silver);
	g1 += silver;
	int gold = g1-g2;
	print(gold);
}
