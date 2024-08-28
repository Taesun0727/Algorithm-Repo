import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        char[][] board = new char[N+1][];
        int[][] jungle = new int[N+1][M+1];
        int[][] sea = new int[N+1][M+1];
        int[][] ice = new int[N+1][M+1];
        for (int i = 1; i <= N; i++) {
            board[i] = br.readLine().toCharArray();
            for (int j = 1; j <= M; j++) {
                jungle[i][j] = jungle[i-1][j] + jungle[i][j-1] - jungle[i-1][j-1];
                ice[i][j] = ice[i-1][j] + ice[i][j-1] - ice[i-1][j-1];
                sea[i][j] = sea[i-1][j] + sea[i][j-1] - sea[i-1][j-1];

                if (board[i][j-1] == 'J') {
                    jungle[i][j]++;
                } else if (board[i][j-1] == 'O') {
                    sea[i][j]++;
                } else {
                    ice[i][j]++;
                }
            }
        }

        int sx, sy, ex, ey;
        int jResult, iResult, sResult;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            sx = Integer.parseInt(st.nextToken());
            sy = Integer.parseInt(st.nextToken());
            ex = Integer.parseInt(st.nextToken());
            ey = Integer.parseInt(st.nextToken());

            jResult = jungle[ex][ey] - jungle[ex][sy-1] - jungle[sx-1][ey] + jungle[sx-1][sy-1];
            iResult = ice[ex][ey] - ice[ex][sy-1] - ice[sx-1][ey] + ice[sx-1][sy-1];
            sResult = sea[ex][ey] - sea[ex][sy-1] - sea[sx-1][ey] + sea[sx-1][sy-1];
            sb.append(jResult + " " + sResult + " " + iResult + " " + "\n");
        }
        System.out.println(sb);
    }
}
