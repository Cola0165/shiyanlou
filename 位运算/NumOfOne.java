public class NumOfOne {
    public static void main(String[] args) {
        System.out.println("1的数量：" + numberOf1(14));
    }
    public static int numberOf1(int n) {
        int num = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                ++num;
            }
            n = n >>> 1;
        }
        return num;
    }
}