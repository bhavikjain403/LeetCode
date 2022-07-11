

bool isPalindrome(int x){
    long int sum=0,n=x;
    if(x<0)
        return false;
    while(x){
        sum=(sum*10)+(long int)x%10;
        x=x/10;
    }
    if(sum==(long int)n)
        return true;
    return false;
}