class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;
        // check if second number is in ascending order
        for (int i = 0; i < n; i++){
            if(nums[i] > nums[(i+1) % n])
            count ++;
            }
        return count <= 1;
    }
}