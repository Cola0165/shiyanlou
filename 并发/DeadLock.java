public class DeadLock {
    public static void main(String[] args) {
        final String eat = "吃饭";
        final String drink = "喝水";
        Thread t1 = new Thread(()->{
            synchronized (eat) {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                synchronized (drink) {
                    // doSomething
                    System.out.println(drink);
                }
            }
        });
        t1.start();
        Thread t2 = new Thread(()->{
            synchronized (drink) {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                synchronized (eat) {
                    // doSomething
                    System.out.println(eat);
                }
            }
        });
        t2.start();
    }
}