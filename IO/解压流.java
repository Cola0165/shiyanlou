import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class 解压流 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String fileZip = "path_to_file.zip";
        File destDir = new File("path_to_dest");
        byte[] buffer = new byte[1024];
        try (ZipInputStream zis = new ZipInputStream(new FileInputStream(fileZip))) {
            ZipEntry zipEntry = zis.getNextEntry();
            while (zipEntry != null) {
                // ...
            }
            zis.closeEntry();
        }
    }
}
