import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static int N;
    static ArrayList<ArrayList<Point>> arr;
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        N = Integer.parseInt(st.nextToken());
        arr = new ArrayList<>(N);
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N+1; i++) {
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            arr.get(a).add(new Point(b, c));
            arr.get(b).add(new Point(a, c));
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            find(s, e);
        }
        System.out.println(sb);

    }

    public static void find(int s, int e) {
        ArrayDeque<Point> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[N+1];
        for (int i = 0; i < arr.get(s).size(); i++) {
            queue.add(arr.get(s).get(i));
            visited[arr.get(s).get(i).x] = true;
        }
        while (!queue.isEmpty()) {
            Point cur = queue.poll();
            if (cur.x == e) {
                sb.append(cur.y + "\n");
            }
            for (int i = 0; i < arr.get(cur.x).size(); i++) {
                Point tmp = arr.get(cur.x).get(i);
                if (!visited[tmp.x]) {
                    queue.add(new Point(tmp.x, tmp.y + cur.y));
                    visited[tmp.x] = true;
                }
            }
        }
    }
}
