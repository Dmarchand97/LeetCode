public class mergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int lenNums1 = m + n;
        int list1Count = 0;
        int list2Count = 0;
       while(list1Count <= m || list2Count <= n){
           int[] tempArray = new int[nums1.length+1];
           //check if either number is zero
           if(nums1[list1Count] == 0){
               //iterate that listCount
               list1Count++;
           }
           if(nums2[list2Count] == 0){
               //iterate that listCount
               list2Count++;
           }
           //check the current numbers in the lists, if l1 <= l2
           if(nums1[list1Count] <= nums2[list2Count]){
               // insert l2[list2Count] into l1[list1Count + 1]
               System.arraycopy(nums1,0, tempArray, 0, list1Count);
               tempArray[list1Count] = nums1[list1Count];
               System.arraycopy(nums1, list1Count, tempArray, list1Count+1, nums1.length);
               // iterate list1Count
               // iterate list2Count
           }

           //else
                // iterate list1Count

       }
    }
}
