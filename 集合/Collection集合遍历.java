import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Collection集合遍历 {
    public static void main(String[] args) {
        
        List<String> array = new ArrayList<String>();
        Iterator<String> it = array.iterator();
            while (it.hasNext()) {
                String s = it.next();
                System.out.println(s);
            }

        for (String str : array) {
            System.out.println(str);
        }

        for (int i = 0; i < array.size(); i++) {
            String s = array.get(i);
            System.out.println(s);
        }
    }      
}
