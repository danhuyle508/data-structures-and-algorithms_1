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

    public Node append(int key){
        Node newNode = new Node();
        newNode.value = key;
        Node current = head;
        while(current != null){
            if(current.next == null){
                current.next = newNode;
                break;
            }
            current = current.next;
        }
        return newNode;
    }

    public Boolean insertBefore(int key, int newValue){
        Node newNode = new Node();
        newNode.value = newValue;
        Node current = head;

        while(current != null){
            if(current.next.value == key){
                newNode.next = current.next;
                current.next = newNode;
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public Boolean insertAfter(int key, int newValue){
        Node newNode = new Node();
        newNode.value = newValue;
        Node current = head;

        while(current != null){
            if(current.value == key){
                newNode.next = current.next;
                current.next = newNode;
                return true;
            }
            current = current.next;
        }
        return false;
    }
}

