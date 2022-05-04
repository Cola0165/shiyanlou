import java.io.File;
import java.io.IOException;

public class File类 {
    public static void main(String[] args) {    
        File file = new File("/tmp/newfile.txt");
        try{
            file.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    } 
    // public static void main(String[] args) throws IOException {
    //     File file = new File("/tmp/newfile.txt");
    //     if(!file.exists()) {
    //         file.createNewFile();
    //     }
        // File file = new File("C:\\newfile.txt");
        //     file.createNewFile();
    // } 
}
