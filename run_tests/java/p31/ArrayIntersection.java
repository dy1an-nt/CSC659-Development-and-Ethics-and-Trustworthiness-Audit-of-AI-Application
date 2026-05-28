import java.util.*;

public class ArrayIntersection {
    public static int[] intersection(int[] arr1, int[] arr2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> resultSet = new HashSet<>();
        for (int num : arr1) set1.add(num);
        for (int num : arr2) {
            if (set1.contains(num)) resultSet.add(num);
        }
        return resultSet.stream().mapToInt(Integer::intValue).toArray();
    }
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {3, 4, 5, 6, 7};
        int[] result = intersection(a, b);
        Arrays.sort(result);
        System.out.println("Intersection: " + Arrays.toString(result));
    }
}
