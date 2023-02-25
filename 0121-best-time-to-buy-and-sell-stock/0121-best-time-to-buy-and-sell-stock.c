

int maxProfit(int* prices, int pricesSize){
    int i,min = prices[0], profit = 0;
    for(i=1;i<pricesSize;i++){
        if(prices[i]<min)
            min = prices[i];
        else if(prices[i]-min>profit)
            profit = prices[i]-min;
    }
    return profit;
}