public class DatabaseConnection {
    private volatile static DatabaseConnection instance;
    private String connectionString;
    private DatabaseConnection() {
        this.connectionString = "jdbc:mysql://localhost:3306/mydb";
        System.out.println("DatabaseConnection created (id: " + System.identityHashCode(this) + ")");
    }
    public static DatabaseConnection getInstance() {
        if (instance == null) {
            synchronized (DatabaseConnection.class) {
                if (instance == null) {
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
    public String getConnectionString() { return connectionString; }
    public static void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            DatabaseConnection db = DatabaseConnection.getInstance();
            System.out.println(Thread.currentThread().getName()
                + " got instance id: " + System.identityHashCode(db));
        };
        Thread[] threads = new Thread[5];
        for (int i = 0; i < 5; i++) {
            threads[i] = new Thread(task, "Thread-" + i);
            threads[i].start();
        }
        for (Thread t : threads) t.join();
    }
}
