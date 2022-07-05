#include <bits/stdc++.h>
#define println(x) cout << x << "\n"
#define print(x) cout << x
#define ti(x) cin >> x
#define input(a, b, c, d, e, f, g, h) cin >> a >> b >> c >> d >> e >> f >> g >> h
#define list vector<long long>
#define min(x) *min_element(x.begin(), x.end())
using namespace std;
int main() {
	int t;
	ti(t);
	long long W, H, x1, y1, x2, y2, w, h, dx1, dx2, dy1, dy2;
	bool qx, qy;
	list d;
	for(int i = 0; i < t; i++) {
		input(W, H, x1, y1, x2, y2, w, h);
		qx = (x2-x1)+w > W;
		qy = (y2-y1)+h > H;
		if(qx && qy) {
			println(-1);
		} else if(!qx && qy) {
			dx1 = w-x1;
			dx2 = x2-W+w;
			if(dx1 <= 0 || dx2 <= 0) {
				println(0);
				continue;
			}
			if(x2 + dx1 <= W) {
				d.push_back(dx1);
			}
			if(x1 - dx2 >= 0) {
				d.push_back(dx2);
			}
			println(min(d));
		} else if(qx && !qy) {
			dy1 = h-y1;
			dy2 = y2-H+h;
			if(dy1 <= 0 || dy2 <= 0) {
				println(0);
				continue;
			}
			if(y2 + dy1 <= H) {
				d.push_back(dy1);
			}
			if(y1 - dy2 >= 0) {
				d.push_back(dy2);
			}
			println(min(d));
		} else {
			dx1 = w-x1;
			dx2 = x2-W+w;
			dy1 = h-y1;
			dy2 = y2-H+h;
			if(dx1 <= 0 || dx2 <= 0 || dy1 <= 0 || dy2 <= 0) {
				println(0);
				continue;
			}
			if(x2 + dx1 <= W) {
				d.push_back(dx1);
			}
			if(x1 - dx2 >= 0) {
				d.push_back(dx2);
			}
			if(y2 + dy1 <= H) {
				d.push_back(dy1);
			}
			if(y1 - dy2 >= 0) {
				d.push_back(dy2);
			}
			println(min(d));
		}
		d.clear();
	}
}
