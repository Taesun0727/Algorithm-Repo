import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static char[][] board;
    static int N, M;
    static int[][][] visited;
    static char[] dirC = new char[]{'U', 'R', 'D', 'L'};
    static int[][] delta = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    static int answerCount = 0;
    static char answerD = 'U';

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];
        visited = new int[N][M][4];
        for (int i = 0; i < N; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = tmp.charAt(j);
            }
        }
        st = new StringTokenizer(br.readLine());
        Point start = new Point(Integer.parseInt(st.nextToken())-1, Integer.parseInt(st.nextToken())-1);

        for (int i = 0; i < 4; i++) {
            init_visited();
            move(start.x, start.y, i, 1);
            int check = answer_check();
            if (check == -1) {
                System.out.println(dirC[i]);
                System.out.println("Voyager");
                return;
            }
            if (answerCount < check) {
                answerD = dirC[i];
                answerCount = check;
            }
        }

        System.out.println(answerD);
        System.out.println(answerCount);

    }

    public static void move(int curX, int curY, int d, int count) {
        visited[curX][curY][d] = count;
//        System.out.println(curX + " " + curY + " " + d + " " + count);
        int nx = curX + delta[d][0];
        int ny = curY + delta[d][1];

        int nd = d;
        if (!range_check(nx, ny) || board[nx][ny] == 'C') {
            return;
        }


        if (board[nx][ny] == '/') {
            if (d == 0) {
                nd = 1;
            } else if (d == 1) {
                nd = 0;
            } else if (d == 2) {
                nd = 3;
            } else {
                nd = 2;
            }
        }

        if (board[nx][ny] == '\\') {
            if (d == 0) {
                nd = 3;
            } else if (d == 1) {
                nd = 2;
            } else if (d == 2) {
                nd = 1;
            } else {
                nd = 0;
            }
        }

        if (visited[nx][ny][nd] != 0) {
            visited[nx][ny][nd] = -1;
            return;
        }
        move(nx, ny, nd, count+1);
    }

    public static void init_visited() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < 4; k++) {
                    visited[i][j][k] = 0;
                }
            }
        }
    }

    public static int answer_check() {
        int maxCount = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < 4; k++) {
                    if (visited[i][j][k] == -1) {
                        return -1;
                    }
                    maxCount = Math.max(maxCount, visited[i][j][k]);
                }
            }
        }
        return maxCount;
    }

    public static boolean range_check(int x, int y) {
        return 0 <= x && N > x && 0 <= y && M > y;
    }
}
