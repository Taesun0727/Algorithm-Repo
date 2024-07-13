import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] visited;
    static int[][] floor;
    static int count;
    static int[][] delta = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        visited = new int[N][M];
        floor = new int[N][M];
        int answer = 0;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            floor[r-1][c-1] = 1;
        }
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (floor[r][c] == 1) {
                    count = 0;
                    findTrash(r, c);
                    if (answer < count) {
                        answer = count;
                    }
                }
            }
        }
        System.out.println(answer);
    }

    static void findTrash(int x, int y) {
        floor[x][y] = 0;
        count++;

        for (int i = 0; i < 4; i++) {
            int nx = x + delta[i][0];
            int ny = y + delta[i][1];
            if (0 > nx || N <= nx || 0 > ny || M <= ny || floor[nx][ny] == 0) {
                continue;
            }
            findTrash(nx, ny);
        }
    }
}
