#include <iostream>
#define println(x) cout << x << "\n"
#define input(x) cin >> x
#define calc(s, v, t) s*v+2*t
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int s, v_one, v_two, t_one, t_two;
	input(s);
	input(v_one);
	input(v_two);
	input(t_one);
	input(t_two);
	int one = calc(s, v_one, t_one);
	int two = calc(s, v_two, t_two);
	if(one < two) {
		println("First");
	} else if(two < one) {
		println("Second");
	} else {
		println("Friendship");
	}
}
