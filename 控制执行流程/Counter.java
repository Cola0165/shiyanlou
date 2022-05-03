import java.util.List;

public class Counter{
    int small = 0;
    int middle = 0;
    int big = 0;
    int huge = 0;
    //... getter methods

    public void read(List<Integer> numbers){
        for(var value: numbers){
            switch(value){
            case 1:
                small += 1;
                break;
            case 2:
                middle += 1;
                break;
            case 3:
                big += 1;
                break;
            default:
                huge +=1;
            }
        }
    }
    public static void main(String[] args) {
    }
}