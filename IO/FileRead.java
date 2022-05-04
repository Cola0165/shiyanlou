import java.io.*;

public class FileRead {
    public static void main(String[] args) throws IOException {
        String filePath = "test.txt";
        File file = new File(filePath);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        String lineString = null;
        while ((lineString = reader.readLine()) != null) {
            System.out.println(lineString);
        }
        reader.close();
    }
}