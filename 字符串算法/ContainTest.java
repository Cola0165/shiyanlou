public class ContainTest {

    public static void main(String[] args) {
      String source = "ABACDABABC";
      String pattern = "BAB";
      System.out.println(isContain(source, pattern));
    }
  
    public static boolean isContain(String source, String pattern) {
      char[] sources = source.toCharArray();
      char[] patterns = pattern.toCharArray();
      // 主串的索引位置
      int i = 0;
      // 模式串的索引位置
      int j = 0;
      while (i < sources.length && j < patterns.length) {
        // 当两个字符相同，就比较下一个
        if (sources[i] == patterns[j]) {
          i++;
          j++;
        } else {
          // 不匹配的时候回溯到开始匹配的下一个索引
          i = i - j + 1;
          // 模式串从头开始匹配
          j = 0;
        }
      }
      if (j == patterns.length) {
        return true;
      } else {
        return false;
      }
    }
  }