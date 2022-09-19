#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(string s) {
    int answer = 0;
    if(s[0]=='+'){
        int n=0;
        for(int i=s.size()-1; i>=1; i--)
            answer+=(s[i]-'0')*pow(10,n++);
    }
    else if(s[0]=='-'){
        int n=0;
        for(int i=s.size()-1; i>=1; i--)
            answer+=(s[i]-'0')*pow(10,n++);
        answer*=-1;
    }
    else{
        int n=0;
        for(int i=s.size()-1; i>=0; i--)
            answer+=(s[i]-'0')*pow(10,n++);
    }
    return answer;
}