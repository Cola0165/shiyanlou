import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class 压缩流 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String sourceFile = "path_to_source";
        File fileToZip = new File(sourceFile);
        try (FileOutputStream fos = new FileOutputStream("path_to_zip");
             FileInputStream fis = new FileInputStream(fileToZip);
             ZipOutputStream zipOut = new ZipOutputStream(fos);) {
            ZipEntry zipEntry = new ZipEntry(fileToZip.getName());
            zipOut.putNextEntry(zipEntry);
            byte[] bytes = new byte[1024];
            int length;
            while ((length = fis.read(bytes)) >= 0) {
                zipOut.write(bytes, 0, length);
            }
        }
    }
}
