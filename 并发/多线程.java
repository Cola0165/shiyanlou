public class 多线程 {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread();
        t.setDaemon(true);
        t.start();
        t.join();
    }
}
