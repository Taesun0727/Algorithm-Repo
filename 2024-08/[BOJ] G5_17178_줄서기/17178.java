import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Node> order = new PriorityQueue<>();
        ArrayList<Node> nodes = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                String tmp = st.nextToken();
                char tmpChar = tmp.charAt(0);  // 'G', 'B', 'A', 'C' 등의 문자를 추출
                int tmpNum = Integer.parseInt(tmp.substring(2));  // '-' 이후의 숫자를 추출
                Node node = new Node(tmpChar, tmpNum);
                nodes.add(node);
                order.add(node);
            }
        }
        Deque<Node> wait = new ArrayDeque<>();
        int index = 0;
        while (!order.isEmpty()) {
            Node tmp = order.peek();

            if (!wait.isEmpty() && tmp.equals(wait.getLast())) {
                order.poll();
                wait.pollLast();
                continue;
            }
            if (index >= N*5) {
                break;
            }
            if (nodes.get(index).equals(tmp)) {
                index++;
                order.poll();
            } else {
                wait.add(nodes.get(index++));
            }
        }


        if (order.isEmpty()) {
            System.out.println("GOOD");
        } else {
            System.out.println("BAD");
        }
    }

    public static class Node implements Comparable<Node> {
        char c;
        int num;
        Node(char c, int num) {
            this.c = c;
            this.num = num;
        }

        @Override
        public int compareTo(Node o) {
            if (this.c != o.c) {
                return this.c - o.c;  // 문자 c를 오름차순으로 비교
            } else {
                return this.num - o.num;  // c가 동일하면 num을 오름차순으로 비교
            }
        }
    }
}
