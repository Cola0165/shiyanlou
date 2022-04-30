import java.util.Properties;

public class Properties类 {
    
    public static void test() {
        Properties properties = System.getProperties();
        properties.list(System.out);
    }
    public static void main(String[] args) {
        test();
    }
}
