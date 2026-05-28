import java.util.*;

public class OrderProcessor {
    record Order(int id, List<Double> items, String customerEmail, String coupon) {}
    static class OrderValidator {
        public boolean validate(Order order) {
            return order.items() != null && !order.items().isEmpty();
        }
    }
    static class PriceCalculator {
        public double calculateSubtotal(List<Double> items) {
            return items.stream().mapToDouble(Double::doubleValue).sum();
        }
        public double applyDiscount(double total, String coupon) {
            if ("SAVE10".equals(coupon)) return total * 0.90;
            return total;
        }
        public double applyTax(double subtotal, double taxRate) {
            return subtotal * (1 + taxRate);
        }
    }
    static class EmailService {
        public void sendConfirmation(String email, double total) {
            System.out.printf("Email sent to %s | Total: $%.2f%n", email, total);
        }
    }
    static class OrderLogger {
        public void log(int orderId) {
            System.out.println("Order #" + orderId + " processed.");
        }
    }
    static void processOrder(Order order) {
        OrderValidator validator = new OrderValidator();
        PriceCalculator calculator = new PriceCalculator();
        EmailService emailService = new EmailService();
        OrderLogger logger = new OrderLogger();
        if (!validator.validate(order)) { System.out.println("Error: invalid order"); return; }
        double subtotal = calculator.calculateSubtotal(order.items());
        subtotal = calculator.applyDiscount(subtotal, order.coupon());
        double total = calculator.applyTax(subtotal, 0.08);
        emailService.sendConfirmation(order.customerEmail(), total);
        logger.log(order.id());
    }
    public static void main(String[] args) {
        Order order = new Order(101, List.of(29.99, 49.99, 14.99), "alice@example.com", "SAVE10");
        processOrder(order);
    }
}
