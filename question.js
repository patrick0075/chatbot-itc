function findINTERGER(array,int){
    for (x = 0 ;x<array.length;x++){
        if (array[x] ==int){
            return x;
         }
    }
}
findINTERGER([1,2,3,4],3);