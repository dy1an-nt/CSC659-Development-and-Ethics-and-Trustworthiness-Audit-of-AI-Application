public class ArrayStack {
    private int[] stack;
    private int top;
    private int capacity;
    public ArrayStack(int capacity) {
        this.capacity = capacity;
        this.stack = new int[capacity];
        this.top = -1;
    }
    public void push(int value) {
        if (top == capacity - 1) throw new RuntimeException("Stack overflow: stack is full.");
        stack[++top] = value;
        System.out.println("Pushed: " + value);
    }
    public int pop() {
        if (isEmpty()) throw new RuntimeException("Stack underflow: stack is empty.");
        return stack[top--];
    }
    public int peek() {
        if (isEmpty()) throw new RuntimeException("Stack is empty.");
        return stack[top];
    }
    public boolean isEmpty() { return top == -1; }
    public static void main(String[] args) {
        ArrayStack stack = new ArrayStack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Peek: " + stack.peek());
        System.out.println("Popped: " + stack.pop());
        System.out.println("Popped: " + stack.pop());
        System.out.println("Is empty: " + stack.isEmpty());
    }
}
