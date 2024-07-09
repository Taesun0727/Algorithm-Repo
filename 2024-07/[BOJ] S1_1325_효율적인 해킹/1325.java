import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static int N, M;
    static ArrayList<Integer>[] arr;
    static boolean[] visited;
    static int[] count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new ArrayList[N+1];
        visited = new boolean[N+1];
        count = new int[N+1];
        for (int i = 0; i < N+1; i++) {
            arr[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());
            arr[first].add(second);
        }

        for (int i = 1; i < N+1; i++) {
            visited = new boolean[N+1];
            BFS(i);
        }
        int maxValue = 0;
        for (int i = 1; i < N+1; i++) {
            maxValue = Math.max(maxValue, count[i]);
        }
        for (int i = 1; i < N+1; i++) {
            if (count[i] == maxValue) {
                System.out.print(i + " ");
            }
        }
    }
    static void BFS(int start) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;

        while(!queue.isEmpty()) {
            int tmp = queue.poll();
            for (int num : arr[tmp]) {
                if (!visited[num]) {
                    count[num]++;
                    visited[num] = true;
                    queue.add(num);
                }
            }
        }
    }
}
