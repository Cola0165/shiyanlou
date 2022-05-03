import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class 资源对象管理 {
    public static void main(String[] args) {
        String filePath = "myfile.txt";
        try (
                InputStream fileStream = new FileInputStream(filePath);
                Scanner scanner = new Scanner(fileStream)
        ) {
            int lineno = 0;
            while (scanner.hasNextLine()) {
                lineno += 1;
                String line = scanner.nextLine();
                System.out.printf("%3d >>> %s%n", lineno, line);
            }
            System.out.println("(EOF)");
        } catch (IOException e) {
            System.err.printf("Error occurred when reading '%s'.%n", filePath);
            System.exit(-1);
        }
    }
}

// public class TestMain {
//     public static void main(String[] args) throws IOException {
//         String filePath = "myfile.txt";
//         InputStream fileStream = null;
//         try {
//             fileStream = new FileInputStream(filePath);
//             Scanner scanner = new Scanner(fileStream);
//             int lineno = 0;
//             while (scanner.hasNextLine()) {
//                 lineno += 1;
//                 String line = scanner.nextLine();
//                 System.out.printf("%3d >>> %s%n", lineno, line);
//             }
//             System.out.println("(EOF)");
//         } catch (IOException e) {
//             System.err.printf("Error occurred when reading '%s'.%n", filePath);
//             System.exit(-1);
//         } finally {
//             if (fileStream != null) {
//                 fileStream.close();
//             }
//         }
//     }
// }