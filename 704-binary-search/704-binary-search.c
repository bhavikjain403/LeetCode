

int search(int* nums, int numsSize, int target){
    int mid,l=0,h=numsSize-1;
    if(numsSize==1)
        if(nums[0]==target)
            return 0;
    while(h-l>1){
        mid = (h+l)/2;
        if(nums[mid]==target)
            return mid;
        if(nums[mid]>target){
            h = mid-1;
        }
        else{
            l = mid+1;
        }
    }
    if(nums[h]==target)
        return h;
    if(nums[l]==target)
        return l;
    return -1;
}