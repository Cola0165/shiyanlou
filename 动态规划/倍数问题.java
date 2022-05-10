import java.util.Scanner;

public class Main {
	static int k;
	static int n;
	static int[][] array;
	static int ans = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		array = new int[k][3];
		int temp;
		int mod;
		for (int i = 0; i < n; i++) {
			temp = sc.nextInt();
			mod = temp % k;
			if (temp >= array[mod][0]) {
				array[mod][2] = array[mod][1];
				array[mod][1] = array[mod][0];
				array[mod][0] = temp;
			} else if (temp >= array[mod][1]) {
				array[mod][2] = array[mod][1];
				array[mod][1] = temp;
			} else if (temp >= array[mod][2]) {
				array[mod][2] = temp;
			}
		}
		int a, b, c, sum, r; // abc分别为我们应该处理的三个数
		// i代表a的行，j代表b的行
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < k; j++) {
				a = array[i][0]; // 选择第一个数字
				// i%k+j%k+r%k=k，且r<k，则可推算出下式
				r = (k - ((i + j) % k)) % k; // 第三个数字模k的值应该为r，即第三个数字应该为第r行
				// 如果第二个数字和第一个数字同组
				if (i == j) {
					b = array[j][1];
					// 如果第三个数字和前两个数字同组
					if (r == i) {
						c = array[r][2];
						// 第三个数字和前两个不同组
					} else {
						c = array[r][0];
					}
				}
				// 第二个数字和第一个数字不同组
				else {
					b = array[j][0];
					// 第三个数字和前两个数字中的某一个同组
					if (r == i || r == j) {
						c = array[r][1];
					}
					// 第三个数字和前两个都不同组
					else {
						c = array[r][0];
					}
				}
				// 应该输出最大的ans
				sum = a + b + c;
				if (sum > ans) {
					ans = sum;
				}
			}
		}
		System.out.println(ans);
		sc.close();
	}
}