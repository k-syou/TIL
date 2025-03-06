package CodingTest.swea.B형.bestApp;

import java.util.Scanner;

interface Constants {
    public static final int WIDTH = 26;
    public static final int HEIGHT = 99;
    public static final int LENGTH = 200;
    public static final int THRESHOLD = 100000007;
}

class Solution {

    private static int value[][] = new int[Constants.HEIGHT][Constants.WIDTH];

    private static Scanner sc;
    private static UserSolution userSolution = new UserSolution();

    private static int init() {
        for (int i = 0; i < Constants.HEIGHT; ++i) {
            for (int j = 0; j < Constants.WIDTH; ++j) {
                value[i][j] = 0;
            }
        }

        int cmd = sc.nextInt();
        return cmd;
    }

    private static int calcChecksum(int value[][], boolean ret) {
        int sum = 0;
        for (int i = 0; i < Constants.HEIGHT; ++i) {
            for (int j = 0; j < Constants.WIDTH; ++j) {
                sum += value[i][j];
                sum %= Constants.THRESHOLD;
            }
        }
        if (!ret)
            ++sum;
        sum %= Constants.THRESHOLD;
        if (sum < 0)
            sum += Constants.THRESHOLD;
        return sum;
    }

    public static void main(String arg[]) throws Exception {
        // System.setIn(new java.io.FileInputStream("sample_input.txt"));
        sc = new Scanner(System.in);
        int T = sc.nextInt();
        int totalScore = 0;
        for (int tc = 1; tc <= T; ++tc) {
            userSolution.initTable();
            int cmd = init();
            int score = 0;

            for (int i = 0; i < cmd; ++i) {
                int row = sc.nextInt();
                int col = sc.nextInt();
                char input[] = sc.next().toCharArray();
                int checksumIn = sc.nextInt();
                if (checksumIn < 0)
                    checksumIn += Constants.THRESHOLD;
                boolean ret = userSolution.updateCell(row, col, input, value);
                int checksum = calcChecksum(value, ret);
                if (checksumIn == checksum)
                    ++score;
            }
            System.out.println("#" + tc + " " + score);
            totalScore += score;
        }
        System.out.println("TotalScore = " + totalScore);
        sc.close();
    }
}