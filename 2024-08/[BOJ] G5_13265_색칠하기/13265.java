import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static ArrayList<ArrayList<Integer>> arr;
    static int[] color;
    static boolean[] visited;
    static boolean answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Tc = Integer.parseInt(br.readLine());
        StringBuffer sb =new StringBuffer();
        for (int tc = 0; tc < Tc; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            arr = new ArrayList<>();
            color = new int[N+1];
            visited = new boolean[N+1];
            answer = false;
            for (int i = 0; i <= N; i++) {
                arr.add(new ArrayList<>());
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr.get(a).add(b);
                arr.get(b).add(a);
            }
            for (int i = 1; i < N+1; i++) {
                if (!arr.get(i).isEmpty() && color[i] == 0) {
                    find(i, 1);
                    if (!answer) {
                        break;
                    }
                }
            }

            if (!answer) {
                sb.append("possible\n");
            } else {
                sb.append("impossible\n");
            }

        }
        System.out.println(sb);
    }

    public static void find(int num, int currentColor) {
        color[num] = currentColor;
        int nextColor;
        int size = arr.get(num).size();
        if (currentColor == 1) {
            nextColor = 2;
        } else {
            nextColor = 1;
        }
        for (int i = 0; i < size; i++) {
            int tmp = arr.get(num).get(i);
            if (color[tmp] == currentColor) {
                answer = true;
                return;
            }
            if (color[tmp] == 0) {
                find(tmp, nextColor);
            }
        }
    }
}
