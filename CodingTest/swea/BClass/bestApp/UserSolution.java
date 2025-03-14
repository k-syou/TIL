package CodingTest.swea.B형.bestApp;

import java.util.ArrayList;
import java.util.List;

class UserSolution {

    private char Table[][][];

    void initTable() {
        // TO DO
        Table = new char[99][26][];
    }

    // 유니온 파인드
    int find(int[] parent, int a) {
        int ra = parent[a];
        if (ra != a) {
            parent[a] = find(parent, ra);
        }
        return parent[a];
    }

    boolean union(int[] parent, int a, int b) {
        int ra = find(parent, a);
        int rb = find(parent, b);
        if (ra != rb) {
            parent[rb] = ra;
            return true;
        }
        return false;
    }

    int[] excelLocToArrayLoc(char[] excelLoc) {
        int[] arrayLoc = new int[2];
        arrayLoc[0] = (int) excelLoc[0];
        arrayLoc[0] -= 65;
        arrayLoc[1] = (int) excelLoc[1];
        arrayLoc[1] -= 48;
        return arrayLoc;
    }

    int arrayLocToIndex(int[] arrayLoc) {
        return arrayLoc[0] * 26 + arrayLoc[1];
    }

    int check(int row, int col, boolean[][] visited, int value[][], int[] parent) {
        if (Table[row][col][0] == '.') {
            visited[row][col] = true;
            value[row][col] = 0;
            return 0;
        }
        if (Table[row][col][0] != '=') {
            int result = Integer.parseInt(new String(Table[row][col]));
            visited[row][col] = true;
            value[row][col] = result;
            return result;
        }
        int[] selfLoc = { row, col };
        int selfIdx = arrayLocToIndex(selfLoc);
        List<Character> ops = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();
        String s = "";
        boolean firstMinus = false;
        for (int i = 1; i < Table[row][col].length; i++) {
            if (Table[row][col][i] == '+') {
                ops.add(Table[row][col][i]);
                continue;
            }
            if (Table[row][col][i] == '-') {
                if (numbers.size() == 0) {
                    firstMinus = true;
                } else {
                    ops.add(Table[row][col][i]);
                }
                continue;
            }
            while (Table[row][col][i] != '+' && Table[row][col][i] != '-') {
                s += Table[row][col][i];
                i += 1;
                if (i == Table[row][col].length) {
                    break;
                }
            }
            char[] c = s.toCharArray();

            if ((int) c[0] >= 65) {
                int[] arrayLoc = excelLocToArrayLoc(c);
                int idx = arrayLocToIndex(arrayLoc);
                if (union(parent, selfIdx, idx)) {

                } else {

                }
            }
        }

        return 0;
    }

    boolean updateCell(int row, int col, char equation[], int value[][]) {
        // TO DO
        Table[row][col] = equation;
        return true; // Need to be changed
    }
}
