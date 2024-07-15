import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        ArrayDeque<Integer> trucks = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            trucks.add(Integer.parseInt(st.nextToken()));
        }
        int time = 0;
        int bridgeWeight = 0;
        ArrayDeque<Integer> bridge = new ArrayDeque<>();
        for (int i = 0; i < W; i++) {
            bridge.add(0);
        }
        while (!bridge.isEmpty()) {
            time++;
            bridgeWeight -= bridge.poll();
            if (!trucks.isEmpty()) {
                if (trucks.peek() + bridgeWeight <= L) {
                    bridgeWeight += trucks.peek();
                    bridge.offer(trucks.poll());
                } else {
                    bridge.offer(0);
                }
            }
        }
        System.out.println(time);
    }
}
