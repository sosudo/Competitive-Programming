#include <bits/stdc++.h>
#include <algorithm>
#define println(x) cout << x << "\n"
#define print(x) cout << x
#define input(a, b, c, d) cin >> a >> b >> c >> d
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6;
	input(x1, y1, x2, y2);
	input(x3, y3, x4, y4);
	input(x5, y5, x6, y6);
	long long W = (y2-y1)*(x2-x1);
	long long B1;
	long long B2;
	long long B3;
	if (!(x1 >= x4 || x2 <= x3 || y1 >= y4 || y2 <= y3)) {
		B1 = (min(y2, y4) - max(y1, y3)) * (min(x2, x4) - max(x1, x3));
	} else {
		B1 = 0;
	}
	if (!(x1 >= x6 || x2 <= x5 || y1 >= y6 || y2 <= y5)) {
		B2 = (min(y2, y6) - max(y1, y5)) * (min(x2, x6) - max(x1, x5));
	} else {
		B2 = 0;
	}
	long long x7, y7, x8, y8;
	x7 = max(x3, x5);
	y7 = max(y3, y5);
	x8 = min(x4, x6);
	y8 = min(y4, y6);
	if (!(x1 >= x8 || x2 <= x7 || y1 >= y8 || y2 <= y7) && !(x3 >= x6 || x4 <= x5 || y3 >= y6 || y4 <= y5)) {
		B3 = (min(y2, y8) - max(y1, y7)) * (min(x2, x8) - max(x1, x7));
	} else {
		B3 = 0;
	}
	long long shown = W-B1-B2+B3;
	if(shown > 0) {
		println("YES");
	} else {
		println("NO");
	}
}
