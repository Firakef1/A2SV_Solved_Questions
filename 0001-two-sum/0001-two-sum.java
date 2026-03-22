import java.util.Arrays;
class Solution {

   public static int findIndex(int[] arr, int target, int startIndex) {
        if (arr == null || startIndex >= arr.length) {
            return -1; // Or handle as appropriate
        }

        for (int i = startIndex; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }


    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        int[] copied = Arrays.copyOf(nums, nums.length);

        Arrays.sort(nums);

        int[] out = new int[2];
        while (left <= right){

            int val = nums[left] + nums[right];
            System.out.println(val);
            if ((int)val == target){
                if (nums[left] == nums[right]){
                    out[0] = findIndex(copied, nums[left], 0);
                    out[1] = findIndex(copied, nums[right], out[0]+1);
                }
                else{
                    out[0] = findIndex(copied, nums[left], 0);
                    out[1] = findIndex(copied, nums[right], 0);
                }
                return out;
            }

            else if (val < target){
                left ++;
            }

            else{
                right --;
            }

        }


        return out;
    }
}