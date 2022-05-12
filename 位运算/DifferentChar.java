public class DifferentChar {

    public static char findDifferentChar(String a, String b) {
        int ret = 0;
        for (int i = 0; i < a.length(); ++i) {
            ret ^= a.charAt(i);
        }
        for (int i = 0; i < b.length(); ++i) {
            ret ^= b.charAt(i);
        }
        return (char) ret;
    }

    public static void main(String[] args) {
        System.out.println(findDifferentChar("lasda","daldas"));
    }
}