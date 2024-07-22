import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        List<Student> list = new ArrayList<>();
        Student[] student = new Student[101];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
        	int studentNum = Integer.parseInt(st.nextToken());
        	if(student[studentNum] == null) {
        		student[studentNum] = new Student(studentNum, 0, 0, false);
        	}
        	if (student[studentNum].isPosted) {
        		student[studentNum].count++;
        	} else {
        		if (list.size() == N) {
        			Collections.sort(list, (o1, o2) -> {
                        if (o1.count != o2.count) {
                            return Integer.compare(o1.count, o2.count);
                        } else {
                            return Integer.compare(o1.time, o2.time);
                        }
                    });
        			list.get(0).isPosted = false;
        			list.remove(0);
        		}
        		student[studentNum].count = 1;
        		student[studentNum].time = i;
        		student[studentNum].isPosted = true;
        		list.add(student[studentNum]);
        	}
        }
        Collections.sort(list, (o1, o2) -> o1.idx - o2.idx);
        for (Student s: list) {
        	System.out.print(s.idx + " ");
        }
    }

    static class Student {
    	int idx;
    	int count;
    	int time;
    	boolean isPosted;
		public Student(int idx, int count, int time, boolean isPosted) {
			super();
			this.idx = idx;
			this.count = count;
			this.time = time;
			this.isPosted = isPosted;
		}
    }
}
