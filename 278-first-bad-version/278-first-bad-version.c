// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int l=1,h=n,mid,pos=1;
    if(n==1)
        return 1;
    while(h>=l){
        mid=l+(h-l)/2;
        if(isBadVersion(mid)){
            h=mid-1;
            pos=mid;
        }
        else
            l=mid+1;
            
    }
    return pos;
}