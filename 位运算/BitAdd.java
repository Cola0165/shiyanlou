public class BitAdd {
    public static void main(String[] args) {
        System.out.println(add(21, 27));
        System.out.println(add(21, -26));
    }

    public static int add(int num1, int num2) {
        while (num2 != 0) {
            // 进位
            int c = (num1 & num2) << 1;
            // 不进位加和结果
            num1 = num1 ^ num2;
            num2 = c;
        }
        return num1;
    }
}