#include <iostream>
#define println(x) cout << x << "\n"
#define input(x) cin >> x
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("paint.in", "r", stdin);
	freopen("paint.out", "w", stdout);
	int a, b, c, d;
	input(a);
	input(b);
	input(c);
	input(d);
	int board[101] = {0};
	for(int i = a; i <= b; i++) {
		board[i] = 1;
	}
	for(int i = c; i <= d; i++) {
		board[i] = 1;
	}
	int ans = 0;
	for(int i = 0; i < 101; i++) {
		if(board[i] == 1 && board[i+1] == 1) {
			ans++;
		}
	}
	println(ans);
}
