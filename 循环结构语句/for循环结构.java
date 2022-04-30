import java.util.HashMap;
import java.util.Map;

public class for循环结构 {
    public static void main(String[] args) {
        
        for (int i = 0; i < 10; i++) {
            System.out.println("Hello World");
        }
        
        String[] arr = new String[] {"1", "2", "3"};
        for (String str : arr) {
            System.out.println("Hello World");
        }
        
        Map<String, String> map = new HashMap<>();
        for (String str : map.keySet()) {
            System.out.println("Hello World");
        }
    }
}
