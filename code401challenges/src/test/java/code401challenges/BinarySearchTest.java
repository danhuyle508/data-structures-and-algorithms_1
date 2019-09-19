package code401challenges;

import org.junit.Test;
import static org.junit.Assert.*;

public class BinarySearchTest {
    @Test
    public void testBinarySearch(){
        assertEquals(
                "this should return the correct index. ",
                2,
                BinarySearch.search(new int[]{1,2,3,4,5,6,7,8,9}, 3)
        );
    }
    @Test
    public void testBinarySearchFail(){
        assertEquals(
                "this should return -1 ",
                -1,
                BinarySearch.search(new int[]{1,2,3,4,5,6,7,8,9}, 11)
        );
    }
    @Test
    public void emptyArray(){
        assertEquals(
        "this should return -1.",
        -1,
                BinarySearch.search(new int[3], 4)
        );
    }
    @Test
    public void singleIndexTest(){
        assertEquals(
                "This should return 0.",
                0,
                BinarySearch.search(new int[]{2}, 2)
        );
    }
}

