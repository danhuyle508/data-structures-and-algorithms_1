package code401challenges;

class Node {
    Node next;
    int value;
}

public class LinkedList {
    Node head;

    public boolean isEmpty(){
        if(head == null){
            return true;
        }
        return false;
    }

    public Node insert(int value){
        Node newNode = new Node();
        newNode.value = value;

        if( head == null){
            head = newNode;
        }
        else{
           Node current = head;
           head = newNode;
           head.next = current;

        }
        return head;
    }

    public boolean includes(int key){
        Node current = head;
        while(current != null){
            if(current.value == key){
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public String toString(){
        StringBuilder list = new StringBuilder("");
        Node current = head;
        while(current != null){
            list.append(current.value + ", ");
            current = current.next;
        }
        return list.toString();
    }
}

