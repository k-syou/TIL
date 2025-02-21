import sys


# trie
# 접두사에 기반한 문제에서 매우 유용한 문제
def build_trie(words):
    """
    'apple' 이라는 단어가 주어지면\n
    'a' → 'p' → 'p' → 'l' → 'e' → '#'\n
    위와 같이 딕셔너리를 만들고,
    후에 'app', 'application' 등의 문자가 온다면\n
    'a' → 'p' → 'p' → 'l' → 'e' → '#'\n
    'app'(...) -->  → '#'\n
    'appl'(...) -->       → 'i' → 'c' → 'a' → 't' → 'i' → 'o' → 'n' → '#'\n

    위와 같이 딕셔너리 구조를 만들어서 '#' 은 도착지로써 작용한다.\n
    즉 'appl' 과 같은 단어를 검색하면 '#'이 없으므로 실패하도록 구성하여 만든다.\n

    :param words: color 문자열 모음
    :return: trie dictionary
    """
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True
    return trie


# init
input = sys.stdin.readline
C, N = map(int, input().split())
colors = [input().replace("\n", "") for _ in range(C)]
names = [input().replace("\n", "") for _ in range(N)]
Q = int(input())
team_names = [input().replace("\n", "") for _ in range(Q)]
trie = build_trie(colors)
names_set = set(names)

res = []
for t_name in team_names:
    found = False  # 찾았는지 여부
    node = trie
    L = len(t_name)

    for i, ch in enumerate(t_name):
        if ch not in node:
            # 현재 노드에서 접두사가 맞는게 없는 경우(즉 color 접두사가 아님)
            break
        node = node[ch]  # 다음 노드
        if "#" in node:  # 다음 노드에 도착지가 있는 경우
            if i < L - 1:  # 마지막 인덱스가 아닌경우
                if t_name[i + 1 :] in names_set:
                    # 접두사를 제외한 단어가 이름 set 에 있는지 확인
                    found = True
                    break

    # 결과 담기
    res.append("Yes" if found else "No")

sys.stdout.write("\n".join(res))


"""
2 2
cc
ccc
ccc
ddd
1
ccccc
"""
