class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0;
        int right = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            int square;
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                square = nums[right];
                right--;
            } else {
                square = nums[left];
                left++;
            }
            result[i] = square * square;
        }
        return result;
    }
}


// Tips and Tricks

// start from the end and iterate backwards to avoid searching for the starting point (first non-negative number which is also the smallest element)

// Since the input array is sorted, begin filling the output array with largest number at output_array[nums.length -1] and moving inwards.  
