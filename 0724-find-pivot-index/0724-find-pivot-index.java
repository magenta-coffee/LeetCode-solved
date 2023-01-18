class Solution {
    
    public int sumArray(int[] arr, int start, int end){
        int sum = 0;
        for (int i = start; i < end; i++){
            sum += arr[i];
        }
        return sum;
    }
    
    public int pivotIndex(int[] nums) {
        if(sumArray(nums, 1, nums.length) == 0){
            return 0; 
        }
        for (int i=1; i < nums.length; i++){
            if(sumArray(nums, 0, i) == sumArray(nums, i+1, nums.length)){
                return i;
            }
        }
        return -1;
    }
}