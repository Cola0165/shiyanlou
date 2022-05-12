import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static String getKSortStr(String str, int k) {
        HashSet<String> set = new HashSet<>();
        // 优先队列
        PriorityQueue<String> queue = new PriorityQueue<>((s1, s2) -> s2.compareTo(s1));
        for (int len = 1; len <= k; len++) {
            for (int i = 0; i < str.length() - len + 1; i++) {
                String substr = str.substring(i, i + len);
                if (!set.contains(substr)) {
                    if (queue.size() < k) {
                        // 直接放
                        queue.offer(substr);
                    } else {
                        // 小于堆顶则取出堆顶，放进去新元素
                        if (substr.compareTo(queue.peek()) < 0) {
                            queue.poll();
                            queue.offer(substr);
                        }
                    }
                    set.add(substr);
                }
            }
        }
        return queue.peek();
    }

    public static void main(String[] args) {
        String s;
        int k;
        Scanner scan = new Scanner(System.in);
        s=scan.next();
        k=scan.nextInt();
        scan.close();
        System.out.println(getKSortStr(s,k));
    }
}