import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class 求和 {
    public static void main(String[] args) {
        Stream<Integer> stream = IntStream.range(0,100).boxed();
        var collector = Collectors.<Integer>summingInt(x->x);
        System.out.println(stream.collect(collector));
    }
}
