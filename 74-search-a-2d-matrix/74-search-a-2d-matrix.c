

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int i=0,j,r=matrixSize,c=*matrixColSize;
    if(matrix[r-1][c-1]>target){
        while(matrix[i][c-1]<target)
            i++;
        for(j=0;j<c;j++){
            if(matrix[i][j]==target)
                return true;
        }
    }
    else if(matrix[r-1][c-1]==target)
        return true;
    return false;
}