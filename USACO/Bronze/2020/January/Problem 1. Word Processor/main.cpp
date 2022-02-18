#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#define print(x) cout << x << "\n"
#define input(x) cin >> x
#define str string
using namespace std;
vector<str> arr;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("word.in", "r", stdin);
	freopen("word.out", "w", stdout);
	int n, k;
	input(n);
	input(k);
	str pre, sentence = "";
	int num = 0;
	str word;
	for(int i = 0; i < n; i++) {
		input(word);
		arr.push_back(word);
	}
	for(str i : arr) {
		sentence.append(i);
		sentence.append(" ");
		num = sentence.size() - count(sentence.begin(), sentence.end(), ' ');
		if(num > k) {
			if(pre.back() == ' ') {
				print(pre.substr(0, pre.size()-1));
			} else {
				print(pre);
			}
			sentence = i;
			sentence.append(" ");
		}
		if(num == k) {
			if(sentence.back() == ' ') {
				print(sentence.substr(0, sentence.size()-1));
			} else {
				print(sentence);
			}
			sentence = "";
		}
		pre = sentence;
	}
	if(sentence != "") {
		if(sentence[sentence.size()-1] == ' ') {
				print(sentence.substr(0, sentence.size()-1));
		} else {
			print(sentence);
		}
	}
}
