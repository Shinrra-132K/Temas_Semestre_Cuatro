class Queue {
	public String[] queue;
	public int front, rear, size, nItems;
	public String nombre;
	public long id;
	
	public Queue (int maxSize){
		size = maxSize;
		queue = new String[size];
		front = -1;
		rear = -1;
		nItems = 0;
	}
	
	public boolean isFull() {
			if(nItems == size) {
				return true;
			} else {
				return false;
			}
	}
	
	public boolean isEmpty() {
		if (nItems == 0) {
			return true;
		} else {
			return false;
		}
	}
	
	public int size() {
		return size;
	}
	
	public int nItem() {
		return nItems;
	}
	
	public void traverse() {
		
		for (int i = 0; i < queue.length; i++) {
			if(queue[i] == null) {
				System.out.println(" ");
			}
			System.out.println(queue[i]);
		}
	}
	
	public void enqueue(String value, long id){
		if (isFull()){
			System.out.println("The Queue is full");
			return;
		}

		if (rear == size - 1){
			rear = -1;
		}

		rear++;
		Long.toString(id);
		queue[rear] = "Nombre: " + value + " " + "Cedula: " + id;
		nItems++;
		if (front == -1)
			front++;
	}
	
	public void dequeue() {
		if (front == size) {
			front = -1;
		}
		
		System.out.println("Persona atendido: " + queue[front]);
		nItems--;
		queue[front] = " ";
		front++;
	}
	
	
}
