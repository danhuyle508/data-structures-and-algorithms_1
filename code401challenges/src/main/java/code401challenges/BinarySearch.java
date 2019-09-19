package code401challenges;

public class BinarySearch {
    public static int search(int[] arr, int num){
        int mid = arr.length/2;
        if(arr[mid] == num){
            return mid;
        }
        if(arr[mid] > num){
            return search(arr, num, 0, mid-1);
        }
        if(arr[mid] < num){
            return search(arr, num, mid + 1, arr.length);
        }
        else{
            return -1;
        }

    }

    public static int search(int[] arr, int num, int start, int end){
        int mid = (start + end)/2;

        if(end != start){

            if(end < start){
                return -1;
            }
            if(arr[mid] > num){
                return search(arr, num, start, mid-1);
            }
            if(arr[mid] < num){
                return search(arr, num, mid + 1, end);
            }
            if(arr[mid] == num){
                return mid;
            }
        }
        return -1;
    }
}
