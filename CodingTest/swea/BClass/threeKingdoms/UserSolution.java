package CodingTest.swea.BClass.threeKingdoms;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class UserSolution {

    class Monarch {
        String monarch;
        int soldier;
        Monarch (String name, int count) {
            monarch = name;
            soldier = count;
        }
        void setName(String name) {
            monarch = name;
        }
        int addSoldier(int mNum) {
            soldier += mNum;
            return soldier;
        }
        int setSoldier(int mNum) {
            soldier = mNum;
            return soldier;
        }
        int dispatch() {
            int result = (int) soldier / 2;
            soldier -= result;
            return result;
        }
    }
    public Monarch[][] mapMonarchs;  // 각 위치별 군대 정보
    public HashMap<String, HashSet<String>> enemy;  // 대표 그룹별 적국 대표 목록
    public HashMap<String, HashSet<String>> member;
    public HashMap<String, String> parent;  // 대표 그룹 (유니온 파인드용)
    public HashMap<String, Integer> rank;
    public HashMap<String, int[]> monarchLoc;  // 각 군주 이름 별 위치
    int SIZE;
    int[] dy = {-1, 0, 1, 0, -1, -1, 1, 1};
    int[] dx = {0, 1, 0, -1, 1, -1, 1, -1};

    String find(String mMonarch) {
        String pMonarchName = parent.get(mMonarch);
        if (!pMonarchName.equals(mMonarch)) {
            parent.put(mMonarch, find(pMonarchName));
        }
        return parent.get(mMonarch);
    }

    void init(int N, int mSoldier[][], char mMonarch[][][])
    {
        mapMonarchs = new Monarch[N][N];
        enemy = new HashMap<>();
        parent = new HashMap<>();
        monarchLoc = new HashMap<>();
        rank = new HashMap<>();
        member = new HashMap<>();
        SIZE = N;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                String name = new String(mMonarch[i][j]);
                mapMonarchs[i][j] = new Monarch(name, mSoldier[i][j]);
                enemy.put(name, new HashSet<>());
                member.put(name, new HashSet<>());
                parent.put(name, name);
                int[] loc = new int[2];
                loc[0] = i;
                loc[1] = j;
                monarchLoc.put(name, loc);
                rank.put(name, 0);
            }
        }
    }

    void destroy()
    {
        
    }
    int ally(char cMonarchA[], char cMonarchB[])
    {
        System.out.println("ally");
        String mMonarchA = new String(cMonarchA);
        String mMonarchB = new String(cMonarchB);
        String pMonarchA = find(mMonarchA);
        String pMonarchB = find(mMonarchB);
        if (pMonarchA.equals(pMonarchB)) {
            return -1;
        }
        HashSet<String> enemyA = enemy.get(pMonarchA);
        if (enemyA.contains(pMonarchB)) {
            return -2;
        }
        if (rank.get(pMonarchA) < rank.get(pMonarchB)) {
            String tmp = pMonarchA;
            pMonarchA = pMonarchB;
            pMonarchB = tmp;
        }
        int rankA = rank.get(pMonarchA);
        int rankB = rank.get(pMonarchB);
        parent.put(pMonarchB, pMonarchA);
        if (rankA == rankB) {
            rank.put(pMonarchA, rankA + 1);
        }
        HashSet<String> memberA = member.get(pMonarchA);
        HashSet<String> memberB = member.get(pMonarchB);
        memberA.addAll(memberB);
        member.remove(pMonarchB);

        HashSet<String> enemyB = enemy.get(pMonarchB);
        enemyA.addAll(enemyB);
        enemyA.add(pMonarchB);
        enemy.remove(pMonarchB);

        for (String tmpName : enemy.get(pMonarchA)) {
            HashSet<String> enemySet = enemy.get(tmpName);
            enemySet.remove(pMonarchB);
            enemySet.add(pMonarchA);
        }
        return 1;
    }
    int attack(char cMonarchA[], char cMonarchB[], char cGeneral[])
    {
        System.out.println("attack");
        String mMonarchA = new String(cMonarchA);
        String mMonarchB = new String(cMonarchB);
        String mGeneral = new String(cGeneral);
        String pMonarchA = find(mMonarchA);
        String pMonarchB = find(mMonarchB);
        // 이미 동맹관계인 경우
        if (pMonarchA.equals(pMonarchB)) {
            return -1;
        }

        // 공격자 부모 주변에 상대방이 있는 지 확인
        int[] locA = monarchLoc.get(pMonarchA);
        int[] locB = monarchLoc.get(mMonarchB);
        ArrayList<String> attackers = new ArrayList<>();
        for (int i = 0; i < 8; i++) {
            int ny = locA[0] + dy[i];
            int nx = locA[1] + dx[i];
            if (ny == locB[0] && nx == locB[1]) {
                attackers.add(mMonarchA);
                break;
            }
        }

        // 부모의 동맹국이 상대방 주변에 있는지 확인
        for (String tmpName : member.get(pMonarchA)) {
            int[] locMember = monarchLoc.get(tmpName);
            for (int i = 0; i < 8; i++) {
                int ny = locMember[0] + dy[i];
                int nx = locMember[1] + dx[i];
                if (ny == locB[0] && nx == locB[1]) {
                    attackers.add(tmpName);
                    break;
                }
            }
        }

        // 동맹국 전체가 공격할 수 없는 상황
        if (attackers.isEmpty()) {
            return -2;
        }

        // 방어국 주변에서 도와주기
        Monarch monarchB = mapMonarchs[locB[0]][locB[1]];
        for (int i = 0; i < 8; i++) {
            int ny = locB[0] + dy[i];
            int nx = locB[1] + dx[i];
            if (ny < 0 || nx < 0 || ny >= SIZE || nx >= SIZE) {
                continue;
            }
            Monarch tmpMonarch = mapMonarchs[ny][nx];
            String tmpPName = parent.get(tmpMonarch.monarch);
            if (!tmpPName.equals(pMonarchB)) {
                continue;
            }
            monarchB.addSoldier(tmpMonarch.dispatch());
        }
        int defenderCount = monarchB.soldier;
        // 출병 병사수 계산
        int attackCount = 0;
        for (String attackName : attackers) {
            int[] locAttack = monarchLoc.get(attackName);
            Monarch attacker = mapMonarchs[locAttack[0]][locAttack[1]];
            attackCount += attacker.dispatch();
        }

        if (attackCount <= defenderCount) {
            // 방어 성공
            monarchB.addSoldier(-attackCount);
            return 0;
        }
        
        // 공격 성공
        HashSet<String> memberA = member.get(pMonarchA);
        HashSet<String> memberB = member.get(pMonarchB);
        HashSet<String> enemyA = enemy.get(pMonarchA);
        HashSet<String> enemyB = enemy.get(pMonarchB);
        
        if (!pMonarchB.equals(mMonarchB)) {
            // 그룹의 대표가 아닌 경우
            // 현재 그룹에서 삭제
            memberB.remove(mMonarchB);
            // 적군 해제
            enemyA.remove(mMonarchB);
            // 이름 변경
            monarchB.setName(mGeneral);
            monarchB.setSoldier(attackCount - defenderCount);
            // 위치 정보 변경
            monarchLoc.remove(mMonarchB);
            monarchLoc.put(mGeneral, locB);
            // 부모 갱신
            for (String tmpName : memberB) {
                find(tmpName);
            }

            // A 그룹으로 편입
            rank.remove(mMonarchB);
            rank.put(mGeneral, 0);
            parent.put(mGeneral, pMonarchA);
            memberA.add(mGeneral);

            // B 그룹에서 적대관계로 설정
            enemyB.add(mGeneral);
        } else {
            // 그룹의 대표인 경우
            if (memberB.isEmpty()) {
                // 혼자인 경우
                member.remove(mMonarchB);
                enemyA.remove(mMonarchB);
                monarchB.setName(mGeneral);
                monarchLoc.remove(mMonarchB);
                monarchLoc.put(mGeneral, locB);
                rank.remove(mMonarchB);
                rank.put(mGeneral, 0);
                parent.put(mGeneral, pMonarchA);
                memberA.add(mGeneral);
            } else {
                String newLeader = memberB.iterator().next();
                HashSet<String> newMember = new HashSet<>();
                for (String tmpName : memberB) {
                    rank.put(tmpName, 0);
                    parent.put(tmpName, newLeader);
                    if (!tmpName.equals(newLeader)) {
                        newMember.add(tmpName);
                    }
                }
                member.put(newLeader, newMember);
                HashSet<String> newEnemy = new HashSet<>();
                for (String tmpName : enemyB) {
                    newEnemy.add(tmpName);
                }

                member.remove(mMonarchB);
                enemyA.remove(mMonarchB);

                monarchB.setName(mGeneral);
                monarchB.setSoldier(attackCount - defenderCount);

                monarchLoc.remove(mMonarchB);
                monarchLoc.put(mGeneral, locB);

                // A 그룹으로 편입
                rank.remove(mMonarchB);
                rank.put(mGeneral, 0);
                parent.put(mGeneral, pMonarchA);
                memberA.add(mGeneral);

                // 적군 설정
                newEnemy.add(mGeneral);
                enemy.put(newLeader, newEnemy);
            }
        }

        return 1;
    }
    int recruit(char cMonarch[], int mNum, int mOption)
    {
        String mMonarch = new String(cMonarch);
        // System.out.println("recruit");
        // System.out.println(mMonarch);
        // for (String key : monarchLoc.keySet()) {
        //     System.out.println(mMonarch);
        //     System.out.println(monarchLoc.get(key).length);
        // }
        int[] loc = monarchLoc.get(mMonarch);

        Monarch currMonarch = mapMonarchs[loc[0]][loc[1]];

        int result = currMonarch.addSoldier(mNum);
        if (mOption == 1) {
            String pName = find(mMonarch);
            for (String tmpName : member.get(pName)) {
                int[] tmpLoc = monarchLoc.get(tmpName);
                Monarch tMonarch = mapMonarchs[tmpLoc[0]][tmpLoc[1]];
                result += tMonarch.addSoldier(mNum);
            }
        }
        return result;
    }
}