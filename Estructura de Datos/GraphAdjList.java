class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

public class GraphAdjList {
    private Node[] adjacencyList;
    private int nodes;

    public GraphAdjList(int nodes) {
        this.nodes = nodes;
        adjacencyList = new Node[nodes];
    }

    public void addEdge(int u, int v) {
        if (u < 0 || u >= nodes || v < 0 || v >= nodes) {
            System.out.println("Invalid edge: (" + u + ", " + v + ")");
            return;
        }
        if (u == v) {
            System.out.println("Self-loops are not allowed: (" + u + ")");
            return;
        }

        Node newNodeV = new Node(v);
        newNodeV.next = adjacencyList[u];
        adjacencyList[u] = newNodeV;

        Node newNodeU = new Node(u);
        newNodeU.next = adjacencyList[v];
        adjacencyList[v] = newNodeU;
    }

    public void printGraph() {
        for (int i = 1; i < nodes; i++) {
            System.out.print("Node " + i + ": ");
            Node temp = adjacencyList[i];
            while (temp != null) {
                System.out.print(temp.value + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }
    
    public void verify(int u, int v) {
    	 if (u < 0 || u >= nodes || v < 0 || v >= nodes) {
             System.out.println("Invalid edge: (" + u + ", " + v + ")");
             return;
         }
         if (u == v) {
             System.out.println("Self-loops are not allowed: (" + u + ")");
             return;
         }
         for (int i = 1; i < nodes; i++) {
			Node temp = adjacencyList[i];
			int existe = 0;
			if (temp != u || temp != v) {
				temp = temp.next;
			} else {
				existe++;
			}
			
			if (existe == 0) {
				System.out.println("No se encuentran conectados");
			} else if (existe == 1) {
				System.out.println("Solo un nodo de los ingresados esta conectados");
			} else {
				System.out.println("Todos los nodos estan conectados");
			}
		}
    }
}

