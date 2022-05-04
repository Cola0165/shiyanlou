import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.util.zip.ZipOutputStream;

public class Zip {
    public static void main(String[] args) throws IOException {
        String zipFileName = "test.zip";
        String fileName = "test.txt";
        File file = new File(fileName);
        ZipOutputStream out = new ZipOutputStream(new FileOutputStream(zipFileName));
        out.putNextEntry(new ZipEntry(""));
        FileInputStream in = new FileInputStream(file);
        int tmp;
        while((tmp = in.read()) != -1) {
            out.write(tmp);
        }
        in.close();
        out.close();
    }
}