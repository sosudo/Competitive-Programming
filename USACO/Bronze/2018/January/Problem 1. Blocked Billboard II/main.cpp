#include <bits/stdc++.h>
#include <string>
#define println(x) cout << x << "\n"
#define print(x) cout << x
#define input(a, b, c, d) cin >> a >> b >> c >> d
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("billboard.in", "r", stdin);
	freopen("billboard.out", "w", stdout);
	int x1, y1, x2, y2, x3, y3, x4, y4, ans;
	input(x1, y1, x2, y2);
	input(x3, y3, x4, y4);
	if(x3 <= x1 && y3 <= y1 && x2 <= x4 && y2 <= y4) {
		ans = 0;
	} else if((y1 == y3 && y2 == y4) || (x1 == x3 && x2 == x4) && ((y1 < y4) || (y3 < y2) || (x3 < x2) || (x1 < x4))) {
		ans = (y2-y1)*(x2-x1) - (min(x2, x4) - max(x1, x3)) * (min(y2, y4) - max(y1, y3));
	} else if((x2 >= x4 && x1 >= x3 && y4 >= y2 && y1 >= y3) || (x2 <= x4 && x1 >= x3 && y2 >= y4 && y1 >= y3) || (x4 >= x2 && x3 >= x1 && y2 <= y4 && y1 >= y3) || (x4 >= x2 && x1 >= x3 && y2 <= y4 && y1 <= y3)) {
		ans = (y2-y1)*(x2-x1) - (min(x2, x4) - max(x1, x3)) * (min(y2, y4) - max(y1, y3));
	} else {
		ans = (y2-y1)*(x2-x1);
	}
	println(ans);
}
