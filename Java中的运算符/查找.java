public class 查找 {
    public int findIn(int[] array, int x){
        for(int i=0; i< array.length; i++){
            if(array[i] == x){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
    }
}
