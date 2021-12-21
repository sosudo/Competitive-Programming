#include <iostream>
#include <string>
#define input(x) cin >> x
#define print(x) cout << x << "\n"
#define str(x) to_string(x)
using namespace std;
int main() {
	string ans;
	long long n;
	input(n);
	ans.append(str(n)+" ");
	while(n != 1) {
		if(n % 2 == 1) {
			n = 3*n + 1;
		} else {
			n = n/2;
		}
		ans.append(str(n)+" ");	
	}
	print(ans);
}
