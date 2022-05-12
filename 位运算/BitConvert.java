public class BitConvert {
    public static String convert(int M, int N) {
        // 如果M=0就直接返回
        if (M == 0) {
            return "0";
        }
        // 符号位记录
        boolean flag = false;
        if (M < 0) {
            flag = true;
            M = -M;
        }
        //对应进制的某一位
        String nums = "0123456789ABCDEF";
        StringBuffer results = new StringBuffer();
        // 直到M等于0
        while (M != 0) {
            // 取余数
            results.append(nums.charAt(M % N));
            M /= N;
        }
        // 翻转
        results.reverse();
        // 还原负数的符号
        if (flag) {
            results.insert(0, "-");
        }
        return results.toString();
    }

    public static void main(String[] args) {
        System.out.println(convert(7,2));
        System.out.println(convert(7,3));
        System.out.println(convert(7,4));

        System.out.println(convert(-31,10));
        System.out.println(convert(-31,13));
        System.out.println(convert(-31,16));
    }
}