import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R, C, K, currentR, currentC;
	static int[][] board;
	static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int[] dir = new int[4];
	static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());
        board = new int[R][C];
        for (int i = 0; i < K; i++) {
        	st = new StringTokenizer(br.readLine());
        	int kR = Integer.parseInt(st.nextToken());
        	int kC = Integer.parseInt(st.nextToken());
        	board[kR][kC] = 1;
        }
        st = new StringTokenizer(br.readLine());
        currentR = Integer.parseInt(st.nextToken());
        currentC = Integer.parseInt(st.nextToken());
        board[currentR][currentC] = 1;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
        	dir[i] = Integer.parseInt(st.nextToken()) - 1;
        }
        count = 0;
        move(0);
        System.out.println(currentR + " " + currentC);

    }

   static void move(int d) {
	   while (true) {
		   int nextR = currentR + delta[dir[d]][0];
		   int nextC = currentC + delta[dir[d]][1];
		   if (canMove(nextR, nextC)) {
			   board[nextR][nextC] = 1;
			   currentR = nextR;
			   currentC = nextC;
			   count = 0;
		   } else {
			   count++;
			   d = (d + 1) % 4;
		   }
		   if (count == 4) {
			   break;
		   }
	   }
   }

    static boolean canMove(int r, int c) {
    	if (0 > r || r >= R || 0 > c || c >= C || board[r][c] != 0) {
    		return false;
    	} else {
    		return true;
    	}
    }
}
