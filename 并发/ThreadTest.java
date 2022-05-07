import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

class Producter extends Thread {
    private BlockingQueue<String> queue;
    private String name;
    public Producter(String name, BlockingQueue<String> queue) {
        this.name = name;
        this.queue = queue;
    }
    @Override
    public void run() {
        for (int i = 0; i < 3; i++) {
            queue.add(name + i);
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
class Consumer extends Thread {
    private BlockingQueue<String> queue;
    public Consumer(BlockingQueue<String> queue) {
        this.queue = queue;
    }
    @Override
    public void run() {
        while (true) {
            if (queue.size() > 0) {
                String task = queue.poll();
                System.out.println(task);
            }
        }
    }
}
public class ThreadTest {
    public static void main(String[] args) {
        BlockingQueue<String> queue = new LinkedBlockingQueue<String>(20);
        // 1
        new Producter("b", queue).start();
        try {
            Thread.sleep(7000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        new Producter("a", queue).start();
        new Consumer(queue).start();
    }
}