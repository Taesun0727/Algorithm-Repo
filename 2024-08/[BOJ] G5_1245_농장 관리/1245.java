import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static int N, M, minHeight, answer;
    static int[][] board;
    static boolean[][] visited;
    static int[][] dt = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visited = new boolean[N][M];
        minHeight = 501;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                board[i][j] = tmp;
                if (tmp < minHeight) {
                    minHeight = tmp;
                }
            }
        }
        answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, board[i][j]);
                }
            }
        }

        System.out.println(answer);

    }

    public static void bfs(int x, int y, int height) {
        Queue<Point> queue = new ArrayDeque<>();
        boolean flag = true;
        queue.add(new Point(x, y));
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            for (int i = 0; i < 8; i++) {
                int nx = p.x + dt[i][0];
                int ny = p.y + dt[i][1];
                if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                    if (board[nx][ny] > height) {
                        flag = false;
                    } else if (!visited[nx][ny] && board[nx][ny] == height) {
                        visited[nx][ny] = true;
                        queue.add(new Point(nx, ny));
                    }
                }
            }
        }
        if (flag && height > minHeight) {
            answer++;
        }
    }

}
