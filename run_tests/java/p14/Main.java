public class Main {
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        int[] testValues = {1, 2, 3, 4, 17, 18, 97};
        for (int n : testValues) {
            System.out.println(n + " is prime: " + isPrime(n));
        }
    }
}
