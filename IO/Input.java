
import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        System.out.print("请开始输入：");
        Scanner scan = new Scanner(System.in);
        String read = scan.nextLine();
        System.out.println("请输入的字符串是："+read);
    }
}

// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;

// public class Input {
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         String input = null;
//         System.out.print("输入数据：");
//         try {
//             input = br.readLine();
//         } catch (IOException e) {
//             e.printStackTrace();
//         } 
//         System.out.println("输入数据：" + input);
//     }
// }

// public class Input {
//     public static void main(String[] args) {
//         char input = '\n';
//         System.out.println("请开始输入：");
//         StringBuilder sb = new StringBuilder();
//         do {
//             try {
//                 input = (char) System.in.read();
//                 sb.append(input);
//             } catch (Exception e) {
//                 e.printStackTrace();
//             }
//         } while (input != '\n');
//         System.out.println("请输入的字符串是：" + sb);
//     }
// }