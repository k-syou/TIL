class UserSolution {
    class OrderStatisticTree {
        private OSTNode root;

        public class OSTNode {
            public int id;
            public int value;
            public int size;
            public int height;
            public OSTNode left, right;

            public OSTNode(int i, int v) {
                id = i;
                value = v;
                size = 1;
            }
        }

        int getSize(OSTNode node) {
            return node == null ? 0 : node.size;
        }

        int height(OSTNode node) {
            return node == null ? 0 : node.height;
        }

        // 노드의 height와 size를 업데이트
        void update(OSTNode node) {
            node.height = 1 + Math.max(height(node.left), height(node.right));
            node.size = 1 + getSize(node.left) + getSize(node.right);
        }

        int getBalance(OSTNode node) {
            return node == null ? 0 : height(node.left) - height(node.right);
        }

        // 오른쪽 회전: Left-Left 케이스
        OSTNode rightRotate(OSTNode y) {
            OSTNode x = y.left;
            OSTNode T2 = x.right;

            // 회전 수행
            x.right = y;
            y.left = T2;

            // 높이와 크기 업데이트
            update(y);
            update(x);
            return x;
        }

        // 왼쪽 회전: Right-Right 케이스
        OSTNode leftRotate(OSTNode x) {
            OSTNode y = x.right;
            OSTNode T2 = y.left;

            // 회전 수행
            y.left = x;
            x.right = T2;

            // 높이와 크기 업데이트
            update(x);
            update(y);
            return y;
        }

        OSTNode balance(OSTNode node) {
            int balance = getBalance(node);

            // Left heavy
            if (balance > 1) {
                // Left-Right 케이스
                if (getBalance(node.left) < 0) {
                    node.left = leftRotate(node.left);
                }
                return rightRotate(node);
            }
            // Right heavy
            if (balance < -1) {
                // Right-Left 케이스
                if (getBalance(node.right) > 0) {
                    node.right = rightRotate(node.right);
                }
                return leftRotate(node);
            }
            return node;
        }

        public OSTNode insert(OSTNode node, int id, int value) {
            if (node == null) {
                return new OSTNode(id, value);
            }
            if (value < node.value) {
                node.left = insert(node.left, id, value);
            } else if (value > node.value) {
                node.right = insert(node.right, id, value);
            } else {
                // 값이 같은 경우, id로 추가 비교 (id에 따라 왼쪽/오른쪽 결정)
                if (id > node.id) {
                    node.left = insert(node.left, id, value);
                } else if (id < node.id) {
                    node.right = insert(node.right, id, value);
                }
            }
            update(node);
            return balance(node);
        }

        OSTNode select(OSTNode node, int k) {
            if (node == null)
                return null;
            int leftSize = getSize(node.left);
            if (k <= leftSize) {
                return select(node.left, k);
            } else if (k > leftSize + 1) {
                return select(node.right, k - leftSize - 1);
            } else {
                return node;
            }
        }

        public int[] select(int k) {
            OSTNode selNode = select(root, k);
            int[] result = new int[2];
            result[0] = selNode.id;
            result[1] = selNode.value;
            return result;
        }

        OSTNode minValueNode(OSTNode node) {
            while (node.left != null) {
                node = node.left;
            }
            return node;
        }

        OSTNode delete(OSTNode node, int id, int value) {
            if (node == null)
                return null;
            if (value < node.value) {
                node.left = delete(node.left, id, value);
            } else if (value > node.value) {
                node.right = delete(node.right, id, value);
            } else {
                // 값이 같은 경우, id에 따른 비교
                if (id > node.id) {
                    // 삽입에서는 id > node.id이면 왼쪽에 넣었으므로,
                    // 삭제 시에도 왼쪽에서 찾아야 합니다.
                    node.left = delete(node.left, id, value);
                } else if (id < node.id) {
                    // 반대로 id < node.id이면 오른쪽 서브트리에서 찾습니다.
                    node.right = delete(node.right, id, value);
                } else {
                    // 해당 노드를 찾은 경우
                    if (node.left == null) {
                        return node.right;
                    } else if (node.right == null) {
                        return node.left;
                    }
                    // 두 자식이 모두 있을 경우, 오른쪽 서브트리에서 최소값(후계자)을 찾음
                    OSTNode successor = minValueNode(node.right);
                    node.value = successor.value;
                    node.id = successor.id;
                    node.right = delete(node.right, successor.id, successor.value);
                }
            }
            // 삭제 후, 높이와 크기 업데이트
            update(node);
            // 삭제 후 균형 맞추기
            return balance(node);
        }

        public void insert(int id, int value) {
            root = insert(root, id, value);
        }

        public void delete(int id, int value) {
            root = delete(root, id, value);
        }

        public int getSize() {
            return root.size;
        }
    }

    OrderStatisticTree[] tree;
    int groupPlayerCount;
    int playerCount;
    int leagueCount;

    void init(int N, int L, int mAbility[]) {
        playerCount = N;
        leagueCount = L;
        groupPlayerCount = (int) N / L;
        tree = new OrderStatisticTree[L];
        for (int g = 0; g < L; g++) {
            tree[g] = new OrderStatisticTree();
            for (int i = 0; i < groupPlayerCount; i++) {
                int idx = g * groupPlayerCount + i;
                tree[g].insert(idx, mAbility[idx]);
            }
            // System.out.println(tree[g].getSize());
        }
    }

    int move() {
        int res = 0;
        int[][] fronts = new int[(leagueCount - 1)][2];
        int[][] backs = new int[(leagueCount - 1)][2];
        for (int i = 0; i < leagueCount - 1; i++) {
            int[] front = tree[i].select(1);
            int[] back = tree[i + 1].select(groupPlayerCount);
            fronts[i] = front;
            backs[i] = back;
            res += front[0] + back[0];
        }

        for (int i = 0; i < fronts.length; i++) {
            tree[i].delete(fronts[i][0], fronts[i][1]);
            tree[i].insert(backs[i][0], backs[i][1]);
            tree[i + 1].delete(backs[i][0], backs[i][1]);
            tree[i + 1].insert(fronts[i][0], fronts[i][1]);
            // System.out.println(tree[i].getSize());
        }
        // System.out.println(res);
        return res;
    }

    int trade() {
        int res = 0;
        int[][] fronts = new int[(leagueCount - 1)][2];
        int[][] backs = new int[(leagueCount - 1)][2];
        for (int i = 0; i < leagueCount - 1; i++) {
            int[] front = tree[i].select((int) (groupPlayerCount + 1) / 2);
            int[] back = tree[i + 1].select(groupPlayerCount);
            fronts[i] = front;
            backs[i] = back;
            res += front[0] + back[0];
        }

        for (int i = 0; i < leagueCount - 1; i++) {
            tree[i].delete(fronts[i][0], fronts[i][1]);
            tree[i].insert(backs[i][0], backs[i][1]);
            tree[i + 1].delete(backs[i][0], backs[i][1]);
            tree[i + 1].insert(fronts[i][0], fronts[i][1]);
            // System.out.println(tree[i].getSize());
        }
        // System.out.println(res);
        return res;
    }
}
/**
 * 1 100
 * 7
 * 100 15 3 1 5 6 8 7 3 2 1 4 5 9 8 7 6 1
 * 200 26
 * 200 30
 * 300 35
 * 300 37
 * 200 27
 * 300 32
 **/
