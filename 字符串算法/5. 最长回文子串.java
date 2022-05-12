public class LongestPalindrome {

    public static void main(String[] args) {
      LongestPalindrome longestPalindrome = new LongestPalindrome();
      System.out.println(longestPalindrome.longestPalindrome("abdbdc"));
    }
  
    // 判断是否是回文串
    public boolean isMatch(String s) {
      int len = s.length();
      for (int i = 0; i < len / 2; i++) {
        // 根据中心判断是否相等
        if (s.charAt(i) != s.charAt(len - i - 1)) {
          return false;
        }
      }
      return true;
    }
  
    public String longestPalindrome(String s) {
      String result = "";
      int max = 0;
      int len = s.length();
      for (int i = 0; i < len; i++)
       for (int j = i + 1; j <= len; j++) {
        // 判断每一段子串
        String str = s.substring(i, j);
        if (isMatch(str) && str.length() > max) {
          result = s.substring(i, j);
          // 记录回文串的最大长度
          max = Math.max(max, result.length());
        }
      }
      return result;
    }
  }