import java.util.List;

public class 循环 {
    public int find(List<String> words, String word) {
        for(int i=0; i < words.size(); i++){
            if(word.equals(words.get(i))){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
    }
}
