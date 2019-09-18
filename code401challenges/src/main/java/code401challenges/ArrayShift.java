//import java.util.Arrays;
package code401challenges;

public class ArrayShift {
    public static int[] arrayShift(int[] old, int num){
        int mid = old.length / 2;
        int[] newArray = new int[old.length + 1];
        int j = 0;
        for(int i = 0; i < newArray.length; i++){
            if(i == mid){
                newArray[i] = num;
            }
            else{
                newArray[i] = old[j];
                j++;
            }
        }
        return newArray;
    }
}
