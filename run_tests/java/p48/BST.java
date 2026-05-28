public class BST {
    private static class Node {
        int value;
        Node left, right;
        Node(int val) { this.value = val; }
    }
    private Node root;
    public void insert(int val) { root = insertRec(root, val); }
    private Node insertRec(Node node, int val) {
        if (node == null) return new Node(val);
        if (val < node.value) node.left = insertRec(node.left, val);
        else if (val > node.value) node.right = insertRec(node.right, val);
        return node;
    }
    public void delete(int val) { root = deleteRec(root, val); }
    private Node deleteRec(Node node, int val) {
        if (node == null) return null;
        if (val < node.value) { node.left = deleteRec(node.left, val); }
        else if (val > node.value) { node.right = deleteRec(node.right, val); }
        else {
            if (node.left == null && node.right == null) return null;
            if (node.left == null) return node.right;
            if (node.right == null) return node.left;
            Node successor = findMin(node.right);
            node.value = successor.value;
            node.right = deleteRec(node.right, successor.value);
        }
        return node;
    }
    private Node findMin(Node node) {
        while (node.left != null) node = node.left;
        return node;
    }
    public void inorder() { inorderRec(root); System.out.println(); }
    private void inorderRec(Node node) {
        if (node == null) return;
        inorderRec(node.left);
        System.out.print(node.value + " ");
        inorderRec(node.right);
    }
    public static void main(String[] args) {
        BST tree = new BST();
        for (int v : new int[]{50, 30, 70, 20, 40, 60, 80}) tree.insert(v);
        System.out.print("Initial (inorder): "); tree.inorder();
        tree.delete(20);
        System.out.print("After deleting 20: "); tree.inorder();
        tree.delete(30);
        System.out.print("After deleting 30: "); tree.inorder();
        tree.delete(50);
        System.out.print("After deleting 50: "); tree.inorder();
    }
}
