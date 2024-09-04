import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = leftPrefix();
        int mid = midPrefix();
        int right = rightPrefix();

        int answer = Math.max(left, Math.max(right, mid));
        System.out.println(answer);

    }

    public static int leftPrefix() {
        int[] sum = new int[arr.length];

        for (int i = arr.length - 2; i >= 1; i--) {
            sum[i] = sum[i+1] + arr[i+1];
        }

        int endSum = sum[1];
        int max = 0;

        for (int i = 2; i < arr.length; i++) {
            max = Math.max(max, endSum - arr[i] + sum[i]);
        }

        return max;
    }

    public static int rightPrefix() {
        int[] sum = new int[arr.length];

        for (int i = 2; i < arr.length; i++) {
            sum[i] = sum[i-1] + arr[i-1];
        }
        int endSum = sum[arr.length - 1];
        int max = 0;

        for (int i = 1; i < arr.length-1; i++) {
            max = Math.max(max, endSum - arr[i] + sum[i]);
        }

        return max;
    }

    public static int midPrefix() {
        int[] leftSum = new int[arr.length];
        int[] rightSum = new int[arr.length];

        for (int i = 2; i < leftSum.length; i++) {
            leftSum[i] = leftSum[i-1] + arr[i];
        }

        for (int i = rightSum.length - 2; i >= 1; i--) {
            rightSum[i] = rightSum[i+1] + arr[i];
        }

        int max = 0;

        for (int i = 1; i < arr.length; i++) {
            max = Math.max(max, leftSum[i] + rightSum[i]);
        }

        return max;
    }
}
