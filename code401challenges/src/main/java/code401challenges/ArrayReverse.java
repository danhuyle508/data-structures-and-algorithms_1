import java.util.Arrays;

// Arrays.toString(array)
public class ArrayReverse{
    public static void main(String[] args){
        int[] startingArray = new int[]{1,2,3,4,5,6};
        System.out.println("old array " + Arrays.toString(startingArray));
        System.out.println("new array " + Arrays.toString(reverseArray(startingArray)));
    }

    public static int[] reverseArray(int[] current){
        int temp;
        for(int i = 0; i<current.length/2;i++){
            // System.out.print("this is current " + current[i]);
            temp = current[current.length - 1 - i];
            current[current.length - 1 - i] = current[i];
            current[i] = temp;
        }
        return current;
    }
}