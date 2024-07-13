import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] sheet = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            sheet[i] = Integer.parseInt(st.nextToken());
        }
        int[] prefixSum = new int[N+1];
        for (int i = 1; i < N; i++) {
            if (sheet[i] > sheet[i+1]) {
                prefixSum[i] = prefixSum[i-1] + 1;
            } else {
                prefixSum[i] = prefixSum[i-1];
            }
        }
        int Q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());
            sb.append(prefixSum[second-1] - prefixSum[first-1]);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
