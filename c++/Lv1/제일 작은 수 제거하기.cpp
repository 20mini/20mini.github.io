#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    if(arr.size()==1)
        answer.push_back(-1);
    else{
        int min_idx=0;
        for(int i=1; i<arr.size(); i++){
            if(arr[min_idx]>arr[i])
                min_idx=i;
        }
        arr.erase(arr.begin()+min_idx);
       answer=arr;
    }
    return answer;
}