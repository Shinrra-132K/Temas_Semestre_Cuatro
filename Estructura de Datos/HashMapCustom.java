private class NodeHashMap {
	int key;
	String value;
	NodeHashMap next;

	NodeHashMap(int key, String value) {
		this.key = key;
		this.value = value;
		this.next = null;
	}
}

class HashMapCustom {
	private NodeHashMap[] table;
	private int capacity;

	public HashMapCustom(int capacity) {
		this.capacity = capacity;
		table = new NodeHashMap[capacity];
	}

	private int hash(int key) {
		return key % capacity;
	}

	public void insert(int key, String value) {
		int index = hash(key);
		NodeHashMap newNode = new NodeHashMap(key, value);

		if (table[index] == null) {
			table[index] = newNode;
		} else {
			NodeHashMap temp = table[index];
			NodeHashMap prev = null;

			while (temp != null) {
				if (temp.key == key) {
					temp.value = value;
					return;
				}
				prev = temp;
				temp = temp.next;
			}

			prev.next = newNode;
		}
	}

	public void traverse() {
		for (int i = 0; i < capacity; i++) {
			System.out.print("Index " + i + ": ");
			NodeHashMap temp = table[i];
			while (temp != null) {
				System.out.print("[" + temp.key + ": " + temp.value + "] -> ");
				temp = temp.next;
			}
			System.out.println("null");
		}
	}

	public int longitud() {
		int count = 0;
		for (int i = 0; i < capacity; i++) {
			NodeHashMap temp = table[i];
			while (temp != null) {
				count++;
				temp = temp.next;
			}
		}
		return count;
	}

	public String getValue(int keyp) {
		int index = hash(keyp);
		NodeHashMap temp = table[index];

		while (temp != null) {
			if (temp.key == keyp) {
				return temp.value;
			}
			temp = temp.next;
		}
		return "No existe mi rey";
	}
}
