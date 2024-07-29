import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	static List<Long> numbers = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        if (10 > N) {
        	System.out.println(N);
        	return;
        } else if (N >= 1023) {
        	System.out.println(-1);
        	return;
        }
        for (int i = 0; i < 10; i++) {
        	search(1, i);
        }
        Collections.sort(numbers);
        System.out.println(numbers.get(N));
    }

    public static void search(int idx, long num) {
    	if (idx > 10) {
    		return;
    	}
    	numbers.add(num);
    	for (int i = 0; i < num % 10; i++) {
    		search(idx+1, num * 10 + i);
    	}

    }
}
