import java.util.*;
import java.util.stream.*;

public class EmployeeAnalysis {
    record Employee(String name, String department, double salary) {}
    public static void main(String[] args) {
        List<Employee> employees = List.of(
            new Employee("Alice",   "Engineering", 95000),
            new Employee("Bob",     "Engineering", 45000),
            new Employee("Charlie", "Marketing",   62000),
            new Employee("Diana",   "Engineering", 110000),
            new Employee("Eve",     "Marketing",   48000),
            new Employee("Frank",   "HR",          55000),
            new Employee("Grace",   "HR",          40000)
        );
        Map<String, Double> avgSalaryByDept = employees.stream()
            .filter(e -> e.salary() > 50000)
            .collect(Collectors.groupingBy(
                Employee::department,
                Collectors.averagingDouble(Employee::salary)
            ));
        System.out.println("Average salary by department (for employees earning > $50,000):");
        avgSalaryByDept.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(entry ->
                System.out.printf("  %-15s $%,.2f%n", entry.getKey(), entry.getValue()));
    }
}
