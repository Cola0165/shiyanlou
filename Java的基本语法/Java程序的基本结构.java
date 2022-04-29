public class Java程序的基本结构 {
    public static void main(String[] args){
        for(int i=0; i<args.length; i++){
            System.out.println(i);
        }
    }
}

// public class App {
//     public int sum(int[] array){
//         int a = 0;
//         for(int i=0; i<array.length; i++){
//             a += array[i];
//         }
//         return a;
//     }
// }

// public interface App {
//     default int sum(int[] array){
//         int a = 0;
//         for(int i=0; i<array.length; i++){
//             a += array[i];
//         }
//         return a;
//     }
// }