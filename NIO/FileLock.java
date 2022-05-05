import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;

public class FileLock {
    public void readFile(String path) {
        RandomAccessFile file = null;
        java.nio.channels.FileLock lock = null;
        try {
            file = new RandomAccessFile(path, "rw");
            FileChannel fileChannel = file.getChannel();
            lock = fileChannel.lock();
            // read and write 
        } catch (IOException e) {
            System.out.println(e);
        } finally {
            if (lock != null) {
                try {
                    lock.release();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (file != null) {
                try {
                    file.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public static void main(String[] args){
    }
}
