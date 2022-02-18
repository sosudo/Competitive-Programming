#include <iostream>
#include <string>
#define print(x) cout << x;
#define input(x) cin >> x;
#define println(x) cout << x << "\n";
#define str string
using namespace std;
int main() {
	str x;
	input(x);
	println(x.at(x.size()-2));
}
