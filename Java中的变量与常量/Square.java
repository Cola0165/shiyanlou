public class Square {
    private int x = 10;
    public int area() {
        return x * x;
    }
    public static void main(String[] args) {
        // place in anywhere runnable

        System.out.println(new Square().area());
    }
}