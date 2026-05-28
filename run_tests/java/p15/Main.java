public class Main {
    public static void main(String[] args) {
        String text = null;
        try {
            int length = text.length();
            System.out.println("Length: " + length);
        } catch (NullPointerException e) {
            System.out.println("Caught NullPointerException: The string is null.");
            System.out.println("Details: " + e.getMessage());
        } finally {
            System.out.println("Finally block always executes.");
        }
        String safeText = (text != null) ? text : "default";
        System.out.println("Safe value: " + safeText);
    }
}
