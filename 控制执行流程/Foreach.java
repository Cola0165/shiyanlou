import java.util.List;

public class Foreach {
    public int words(List<String> content){
        int count = 0;
        for(var str: content){
            var tokens = str.split(" ");
            count += tokens.length;
        }
        return count;
    }    public static void main(String[] args) {
    }
}
