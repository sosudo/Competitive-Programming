#include <iostream>
#include <algorithm>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
#define run(n, x) for(int x = 0; x < n; x++)
#define inc(a, b) do{input(b);a += b;}while(0)
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	input(n);
	int ans = 0;
	int count = 0;
	int a;
	run(n, i){
		run(3, j) {
			inc(count, a);
		}
		if(count >= 2) {
			ans += 1;
		}
		count = 0;
	}
	print(ans);
}
