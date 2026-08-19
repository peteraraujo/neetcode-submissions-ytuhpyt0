class Solution {
    public int[] getConcatenation(int[] nums) {

        int size = nums.length;

        int[] res = new int[2 * size];

        for (int i = 0; i < size; i++) {
            res[i] = res[i + size] = nums[i];
        }

        return res;

        
    }
}