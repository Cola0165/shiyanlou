// import java.util.function.IntPredicate;
import java.util.stream.IntStream;

public class 过滤 {
    public static void main(String[] args) {
        IntStream stream=IntStream.range(0,100);
        System.out.println(stream.filter(x->x%2==0));

    //     System.out.println(stream.filter(x->{
    //     return x%2==0;
    // }));
    
    // IntPredicate filter = new IntPredicate() {
    //         @Override
    //         public boolean test(int value) {
    //                 return value % 2 == 0;
    //         }
    //     };
    //     System.out.println(stream.filter(filter));
    }
}
