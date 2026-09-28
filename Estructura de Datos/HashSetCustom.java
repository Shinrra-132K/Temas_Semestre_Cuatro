private static class NodeHashSet {
    int key;
    NodeHashSet next;

    NodeHashSet(int key) {
        this.key = key;
        this.next = null;
    }
}

class HashSetCustom {
    private NodeHashSet[] table;
    private int capacity;
    
    public HashSetCustom(int capacity) {
        this.capacity = capacity;
        table = new NodeHashSet[capacity];
    }

    private int hash(int key) {
        return key % capacity;
    }

    public void insert(int key) {
        int index = hash(key);
        NodeHashSet temp = table[index];

        while (temp != null) {
            if (temp.key == key) {
                return; 
            }
            temp = temp.next;
        }

        NodeHashSet newNode = new NodeHashSet(key);
        newNode.next = table[index];
        table[index] = newNode;
    }

    public void traverse() {
        for (int i = 0; i < capacity; i++) {
            System.out.print("Index " + i + ": ");
            NodeHashSet temp = table[i];
            while (temp != null) {
                System.out.print(temp.key + " -> ");
                temp = temp.next;
            }
            System.out.println("null");
        }
    }
}

