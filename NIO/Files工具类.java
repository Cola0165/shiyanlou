import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Files工具类 {
    // 判断文件是否存在
    public Boolean isExists(String filePath) {
        Path path = Paths.get(filePath);
        return Files.exists(path, new LinkOption[]{ LinkOption.NOFOLLOW_LINKS});
    }
    // 创建文件
    public void createFile(String filePath) throws IOException {
        Path path = Paths.get(filePath);
        Files.createFile(path);
    }
    // 删除文件
    public void deleteFile(String filePath) throws IOException {
        Path path = Paths.get(filePath);
        Files.delete(path);
    }
    public static void main(String[] args){
    }
}
