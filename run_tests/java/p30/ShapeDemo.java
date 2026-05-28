public class ShapeDemo {
    static class Shape {
        public double calculateArea() { return 0.0; }
        public String describe() { return "I am a Shape with area: " + calculateArea(); }
    }
    static class Circle extends Shape {
        private double radius;
        public Circle(double radius) { this.radius = radius; }
        @Override
        public double calculateArea() { return Math.PI * radius * radius; }
        @Override
        public String toString() {
            return String.format("Circle (radius=%.2f) -> Area: %.4f", radius, calculateArea());
        }
    }
    static class Rectangle extends Shape {
        private double width, height;
        public Rectangle(double width, double height) { this.width = width; this.height = height; }
        @Override
        public double calculateArea() { return width * height; }
    }
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(5.0), new Rectangle(4.0, 6.0) };
        for (Shape s : shapes) {
            System.out.println(s.describe());
        }
        Circle c = new Circle(3.0);
        System.out.println(c);
    }
}
