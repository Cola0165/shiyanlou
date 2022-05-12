public class LongestPalindrome {

  public static void main(String[] args) {
    LongestPalindrome longestPalindrome = new LongestPalindrome();
    System.out.println(longestPalindrome.findLongestPalindrome("abdbdc"));
  }

  public String findLongestPalindrome(String str) {
    if (str == null || str.length() < 2) {
      return str;
    }
    int maxLen = 1;
    String result = str.substring(0, 1);
    for (int i = 0; i < str.length() - 1; i++) {
      // 中心为 i 的奇数个回文串
      String odd = spread(str, i, i);
      // 中心为 i 和 i+1 的偶数个回文串
      String even = spread(str, i, i + 1);
      // 先比较出两者最长的
      String max = odd.length() > even.length() ? odd : even;
      // 与之前记录的最长回文串比较
      if (max.length() > maxLen) {
        // 更新最长串
        maxLen = max.length();
        result = max;
      }
    }
    return result;
  }

  private String spread(String str, int left, int right) {
    int len = str.length();
    while (left >= 0 && right < len) {
      if (str.charAt(left) == str.charAt(right)) {
        left--;
        right++;
      } else {
        break;
      }
    }
    return str.substring(left + 1, right);
  }
}