public class HammingDistance {
    public static int hammingDistance(int x, int y) {
        int s = x ^ y, result = 0;
        while (s != 0) {
            result += s & 1;
            s >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("汉明距离：" + hammingDistance(83, 53));
    }
}

// public class HammingDistance {
//     public static int hammingDistance(int x, int y) {
//         int s = x ^ y, result = 0;
//         while (s != 0) {
//             s &= s - 1;
//             result++;
//         }
//         return result;
//     }

//     public static void main(String[] args) {
//         System.out.println("汉明距离：" + hammingDistance(83, 53));
//     }
// }