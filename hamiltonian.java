import java.util.Arrays;

public class HamiltonianCycle {

    private boolean isSafe(int v, int[][] graph, int[] path, int pos) {
        if (graph[path[pos - 1]][v] == 0) {
            return false;
        }

        for (int i = 0; i < pos; i++) {
            if (path[i] == v) {
                return false;
            }
        }

        return true;
    }

    private boolean solve(int[][] graph, int[] path, int pos, int n) {
        if (pos == n) {
            return graph[path[n - 1]][path[0]] == 1;
        }

        for (int v = 1; v < n; v++) {
            if (isSafe(v, graph, path, pos)) {
                path[pos] = v;

                if (solve(graph, path, pos + 1, n)) {
                    return true;
                }

                path[pos] = -1;
            }
        }

        return false;
    }

    public int[] findHamiltonianCycle(int[][] graph) {
        int n = graph.length;
        int[] path = new int[n];
        Arrays.fill(path, -1);

        path[0] = 0;

        if (!solve(graph, path, 1, n)) {
            return null;
        }

        int[] result = new int[n + 1];
        System.arraycopy(path, 0, result, 0, n);
        result[n] = path[0];

        return result;
    }

    public static void main(String[] args) {
        HamiltonianCycle hc = new HamiltonianCycle();

        int[][] graph1 = {
            {0, 1, 0, 1, 0},
            {1, 0, 1, 1, 1},
            {0, 1, 0, 0, 1},
            {1, 1, 0, 0, 1},
            {0, 1, 1, 1, 0}
        };

        int[] cycle1 = hc.findHamiltonianCycle(graph1);
        if (cycle1 != null) {
            System.out.println("Cycle exists: " + Arrays.toString(cycle1));
        } else {
            System.out.println("No Hamiltonian Cycle exists.");
        }

        int[][] graph2 = {
            {0, 1, 0, 1, 0},
            {1, 0, 1, 1, 1},
            {0, 1, 0, 0, 1},
            {1, 1, 0, 0, 0},
            {0, 1, 1, 0, 0}
        };

        int[] cycle2 = hc.findHamiltonianCycle(graph2);
        if (cycle2 != null) {
            System.out.println("Cycle exists: " + Arrays.toString(cycle2));
        } else {
            System.out.println("No Hamiltonian Cycle exists.");
        }
    }
}
