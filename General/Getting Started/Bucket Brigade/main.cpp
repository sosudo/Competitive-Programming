#include <iostream>
#include <algorithm>
#include <string>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
#define str string
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("buckets.in", "r", stdin);
	freopen("buckets.out", "w", stdout);
	int by, byfinal, bxfinal, ly, lyfinal, lxfinal, ry, ryfinal, rxfinal;
	bool db = false, dl = false, dr = false;
	string x;
	for(int i = 0; i < 10; i++) {
		input(x);
		if(count(x.begin(), x.end(), 'B') == 1) {
			byfinal = by;
			bxfinal = x.find_first_of('B');
			db = true;
		}
		if(count(x.begin(), x.end(), 'L') == 1) {
			lyfinal = ly;
			lxfinal = x.find_first_of('L');
			dl = true;
		}
		if(count(x.begin(), x.end(), 'R') == 1) {
			ryfinal = ry;
			rxfinal = x.find_first_of('R');
			dr = true;
		}
		by++;
		ly++;
		ry++;
		if(db && dl && dr) {
			break;
		}
	}
	int ans = abs(byfinal-lyfinal)+abs(bxfinal-lxfinal)-1;
	if(bxfinal == lxfinal && lxfinal == rxfinal && ((byfinal < ryfinal && ryfinal < lyfinal) || (lyfinal < ryfinal && ryfinal < byfinal))) {
		ans += 2;
	} else if(byfinal == lyfinal && lyfinal == ryfinal && ((bxfinal < rxfinal && rxfinal < lxfinal) || (lxfinal < rxfinal && rxfinal < bxfinal))) {
		ans += 2;
	} else {}
	print(ans);
}
