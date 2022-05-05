import java.nio.DoubleBuffer;

public class BufferTest {
    public static void main(String[] args) {
        DoubleBuffer doubleBuffer = DoubleBuffer.allocate(10);
        doubleBuffer.put(12.0);
        doubleBuffer.put(25.0);
        doubleBuffer.flip();
        System.out.println(doubleBuffer.get());
        System.out.println(doubleBuffer.get());
        doubleBuffer.clear();
    }
}