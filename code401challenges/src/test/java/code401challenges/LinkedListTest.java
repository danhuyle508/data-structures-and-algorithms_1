package code401challenges;

import org.junit.Test;

import static org.junit.Assert.*;

public class LinkedListTest {
    LinkedList randomList = new LinkedList();
    @Test
    public void insertTest(){

        assertEquals(
                "This should give back 5.",
                5,
                randomList.insert(5).value
        );
    }

    @Test
    public void insertManyTest(){
        randomList.insert(5);
        randomList.insert(6);
        randomList.insert(7);
        assertEquals(
                "This should give back 8.",
                8,
                randomList.insert(8).value
        );
    }

    @Test
    public void includesTest(){
        randomList.insert(5);
        randomList.insert(6);
        randomList.insert(7);
        assertTrue(
                "This should give back true.",
                randomList.includes(6)
        );
    }

    @Test
    public void includesTestFail(){
        randomList.insert(5);
        randomList.insert(6);
        randomList.insert(7);
        assertFalse(
                "This should give back false.",
                randomList.includes(10)
        );
    }

    @Test
    public void printTest(){
        randomList.insert(5);
        randomList.insert(6);
        randomList.insert(7);
        assertEquals(
                "This should give back all values.",
                "7, 6, 5, ",
                randomList.toString()
        );
    }

    @Test
    public void emptyTest(){
        assertTrue(
                "This should give back true.",
                randomList.isEmpty()
        );
    }
}