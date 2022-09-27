#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    int k=b>a?b-a+1:a-b+1;
    answer=(long long)(a+b)*k/2;
    return answer;
}