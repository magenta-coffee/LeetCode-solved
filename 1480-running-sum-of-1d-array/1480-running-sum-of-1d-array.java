class Solution {
    public int[] runningSum(int[] nums) {
        int sum[] = nums.clone();
        for (int i = 1; i < nums.length; i++){
            sum[i] = sum[i-1] + nums[i];
        }
        return sum;
    }
}