

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i,j;
    *returnSize=2;
    returnSize=(int*)malloc(2*sizeof(int));
    i=0;
    j=numbersSize-1;
    while(j>i){
        if(numbers[j]+numbers[i]==target){
            returnSize[0]=i+1;
            returnSize[1]=j+1;
            return returnSize;
        }
        else if(numbers[j]+numbers[i]>target)
            j--;
        else
            i++;
    }
    return numbers;
}