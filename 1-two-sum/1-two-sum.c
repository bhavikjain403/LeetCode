

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i,j;
    *returnSize=2;
    returnSize=(int*)malloc(2*sizeof(int));
    for(i=0;i<numsSize;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                returnSize[0]=i;
                returnSize[1]=j;
                return returnSize;
            }
        }
    }
    return 0;
}