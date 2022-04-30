public class 查找最大值 {
    int max(int[] array){
        if(array.length == 0){
            return 0;
        }
        int result = array[0];
        for(int i=1;i<array.length;i++){
            int value = array[i];
            if(value > result){
                result = value;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    }
}
