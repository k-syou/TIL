
import java.util.HashMap;
import java.util.Map;

class UserSolution {

    class Area {
        private int soldierCount;
        private char[] kingName;
        public int index;

        public Area(int s_count, char[] k_name, int i) {
            soldierCount = s_count;
            kingName = k_name;
            index = i;
        }

        public char[] getKingName() {
            return kingName;
        }

        public int getSoldierCount() {
            return soldierCount;
        }

        public void setSoldierCount(int increase) {
            soldierCount += increase;
        }

        public int find_team() {
            return find(parent, index);
        }

    }

    int find(int[] p, int a) {
        int root = p[a];
        if (root != a) {
            p[a] = find(p, p[a]);
        }
        return p[a];
    }

    boolean union(int[] p, int[] rank, int a, int b) {
        int rootA = find(p, a);
        int rootB = find(p, b);
        if (rootA != rootB) {
            if (rank[rootA] > rank[rootB]) {
                p[rootB] = rootA;
            } else if (rank[rootA] < rank[rootB]) {
                p[rootA] = rootB;
            } else {
                rank[rootA] += 1;
                p[rootB] = rootA;
            }
            return true;
        }
        return false;
    }

    public Area[][] area;
    public Map<char[], int[]> mapping;
    public static int[] parent;
    public static int[] rank;

    void init(int N, int mSoldier[][], char mMonarch[][][]) {
        parent = new int[N * N];
        rank = new int[N * N];
        area = new Area[N][N];
        mapping = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                area[i][j] = new Area(mSoldier[i][j], mMonarch[i][j], i * N + j);
                int[] loc = { i, j };
                mapping.put(area[i][j].getKingName(), loc);
                int index = area[i][j].index;
                parent[index] = index;
                rank[index] = 0;
            }
        }
    }

    void destroy() {

    }

    int ally(char mMonarchA[], char mMonarchB[]) {
        if (mMonarchA.equals(mMonarchB)) {
            return -1;
        }
        int[] locA = mapping.get(mMonarchA);
        int[] locB = mapping.get(mMonarchB);
        union(parent, rank, area[locA[0]][locA[1]].index, area[locB[0]][locB[1]].index);
        return -4;
    }

    int attack(char mMonarchA[], char mMonarchB[], char mGeneral[]) {
        return -3;
    }

    int recruit(char mMonarch[], int mNum, int mOption) {
        return -1;
    }
}
