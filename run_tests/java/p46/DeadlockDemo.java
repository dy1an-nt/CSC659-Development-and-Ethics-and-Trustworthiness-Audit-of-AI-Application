public class DeadlockDemo {
    static final Object LOCK_A = new Object();
    static final Object LOCK_B = new Object();
    static class SafeThread1 implements Runnable {
        public void run() {
            synchronized (LOCK_A) {
                synchronized (LOCK_B) {
                    System.out.println("SafeThread1: both locks acquired");
                }
            }
        }
    }
    static class SafeThread2 implements Runnable {
        public void run() {
            synchronized (LOCK_A) {
                synchronized (LOCK_B) {
                    System.out.println("SafeThread2: both locks acquired");
                }
            }
        }
    }
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Safe version ===");
        Thread t1 = new Thread(new SafeThread1());
        Thread t2 = new Thread(new SafeThread2());
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println("Completed without deadlock.");
    }
}
