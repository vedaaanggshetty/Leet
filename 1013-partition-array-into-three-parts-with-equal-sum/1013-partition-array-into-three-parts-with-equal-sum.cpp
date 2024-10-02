class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int count = 0;
        int sum = 0;
        for (int c : arr){
           sum += c;
        }
        int total = sum / 3;
        int n = arr.size();
        int cur = 0;

        if(sum % 3 != 0)
        return false;

        for(int i = 0; i < n; i++){
            cur += arr[i];
            if (cur == total){
                cur = 0;    
                count++;
            }
            if(count == 2 && i < arr.size() -1){
            return true;
            }
        }
        
        return false;
    }
};