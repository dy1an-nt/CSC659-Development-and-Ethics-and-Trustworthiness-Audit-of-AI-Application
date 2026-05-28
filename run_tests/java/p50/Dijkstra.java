import java.util.*;

public class Dijkstra {
    static final int INF = Integer.MAX_VALUE;
    public static int[] dijkstra(int[][] graph, int source) {
        int n = graph.length;
        int[] dist = new int[n];
        boolean[] visited = new boolean[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, source});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[1];
            if (visited[u]) continue;
            visited[u] = true;
            for (int v = 0; v < n; v++) {
                if (graph[u][v] != 0 && !visited[v]) {
                    long newDist = (long) dist[u] + graph[u][v];
                    if (newDist < dist[v]) {
                        dist[v] = (int) newDist;
                        pq.offer(new int[]{dist[v], v});
                    }
                }
            }
        }
        return dist;
    }
    public static void main(String[] args) {
        int[][] graph = {
            {0, 4, 0, 0, 0, 0, 0, 8, 0},
            {4, 0, 8, 0, 0, 0, 0, 11, 0},
            {0, 8, 0, 7, 0, 4, 0, 0, 2},
            {0, 0, 7, 0, 9, 14, 0, 0, 0},
            {0, 0, 0, 9, 0, 10, 0, 0, 0},
            {0, 0, 4, 14, 10, 0, 2, 0, 0},
            {0, 0, 0, 0, 0, 2, 0, 1, 6},
            {8, 11, 0, 0, 0, 0, 1, 0, 7},
            {0, 0, 2, 0, 0, 0, 6, 7, 0}
        };
        int source = 0;
        int[] distances = dijkstra(graph, source);
        System.out.println("Shortest distances from vertex " + source + ":");
        for (int i = 0; i < distances.length; i++) {
            System.out.printf("  To vertex %d: %d%n", i, distances[i]);
        }
    }
}
