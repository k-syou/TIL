import java.util.Scanner;

public class Solution {
    public static String[] dfs(String[][] starDp, int i) {
        if (starDp[i] != null) {
            return starDp[i];
        }
        String[] beforeStar = dfs(starDp, i - 1);
        String[] nowStar;
        if (i % 3 == 0) {
            int nowStarLength = beforeStar.length + 1;
            nowStar = new String[nowStarLength];
            int starCnt = beforeStar[0].length();
            String addStar = "";
            for (int s = 0; s < starCnt; s++) {
                addStar += "*";
            }
            for (int j = 0; j < nowStarLength - 1; j++) {
                nowStar[j] = beforeStar[j];
            }
            nowStar[nowStarLength - 1] = addStar;
        } else if (i % 3 == 1) {
            int nowStarLength = beforeStar.length * 2;
            nowStar = new String[nowStarLength];
            for (int j = 0; j < nowStarLength; j++) {
                nowStar[j] = beforeStar[j % beforeStar.length];
            }
        } else {
            int nowStarLength = beforeStar.length;
            nowStar = new String[nowStarLength];
            int spaceCnt = (int) i / 3 + 1;
            String space = "";
            for (int j = 0; j < spaceCnt; j++) {
                space += " ";
            }
            for (int j = 0; j < nowStarLength; j++) {
                nowStar[j] = beforeStar[j] + space + "*";
            }
        }
        starDp[i] = nowStar;
        return starDp[i];
    }

    public static String[][] starDp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int T;
        starDp = new String[37][];
        starDp[1] = new String[1];
        starDp[1][0] = "*";

		T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
		{
            System.out.println(String.format("#%d", test_case));
            int N = sc.nextInt();
            String[] stars = dfs(starDp, N);
            for (int i = 0; i < stars.length; i++) {
                System.out.println(stars[i]);
            }
		}
        sc.close();
    }
}