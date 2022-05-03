import java.util.Random;

public class 函数的重载 {
    private static final Random random = new Random();

    private static double gaussian() {
        return gaussian(0, 1);
    }

    private static double gaussian(double sigma2) {
        return gaussian(0, sigma2);
    }

    private static double gaussian(double mu, double sigma2) {
        return Math.sqrt(sigma2) * random.nextGaussian() + mu;
    }
    public static void main(String[] args) {
        System.out.println(gaussian());
        System.out.println(gaussian(1));
        System.out.println(gaussian(0,1));
    }
}