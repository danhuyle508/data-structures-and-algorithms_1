import java.util.Arrays;

// Arrays.toString(array)
public class ArrayReverse{
    public static void main(String[] args){
        int[] startingArray = new int[]{1,2,3,4,5,6};
        System.out.println("old array " + Arrays.toString(startingArray));
        System.out.println("new array " + Arrays.toString(reverseArray(startingArray)));
    }

    public static int[] reverseArray(int[] current){
        int[] newArray = new int[current.length];
        for(int i = 0; i<current.length;i++){
            newArray[i] = current[current.length - 1 - i];
        }
        return newArray;
    }
}