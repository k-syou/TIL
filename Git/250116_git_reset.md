# git reset

`git reset` 명령어는 Git에서 커밋을 취소하거나 특정 커밋으로 되돌리는 데 사용됩니다. 이 명령어는 세 가지 주요 모드로 작동합니다: `--soft`, `--mixed`, `--hard`.
마치 시계를 과거로 되돌리는 듯한 행위입니다. 하지만 기록에는 남아있어서 접근이 가능합니다.

## 사용법

```bash
git reset <option> <commit-hash>
```

### <option> 설명

- `--soft`
    1. Stage : O
    2. Working Directory : O
    3. Commit History : X

- `--mixed`
    1. Stage : X
    2. Working Directory : O
    3. Commit History : X
- `--hard`
    1. Stage : X
    2. Working Directory : X
    3. Commit History : X

    ### 용어 설명
    - **Stage (인덱스)**: Stage는 커밋을 만들기 전에 파일의 스냅샷을 저장하는 영역입니다. 파일을 Stage에 추가하면, 해당 파일은 다음 커밋에 포함될 준비가 된 것입니다. `git add` 명령어를 사용하여 파일을 Stage에 추가할 수 있습니다.
        - git status
    - **Working Directory (작업 디렉토리)**: Working Directory는 현재 작업 중인 파일들이 있는 디렉토리입니다. 여기서 파일을 수정하고, 추가하고, 삭제할 수 있습니다. Working Directory의 변경 사항은 Stage에 추가되기 전까지 Git의 추적을 받지 않습니다.
        - ls -l
    - **Commit History (커밋 히스토리)**: Commit History는 프로젝트의 모든 커밋을 시간 순서대로 나열한 기록입니다. 각 커밋은 고유한 해시 값을 가지며, 프로젝트의 특정 시점의 상태를 나타냅니다. `git log` 명령어를 사용하여 Commit History를 확인할 수 있습니다.
        - git log --oneline

### 예시

1. 마지막 커밋을 취소하고 변경 사항을 인덱스에 유지:

    ```bash
    git reset --soft HEAD~1
    ```

2. 마지막 커밋을 취소하고 변경 사항을 작업 디렉토리에 유지:

    ```bash
    git reset --mixed HEAD~1
    ```

3. 마지막 커밋을 취소하고 모든 변경 사항을 삭제:

    ```bash
    git reset --hard HEAD~1
    ```

### 복구 방법

`git reset` 명령어를 잘못 사용하여 중요한 커밋을 삭제했더라도, `git reflog` 명령어를 사용하여 복구할 수 있습니다. `git reflog`는 Git의 모든 참조 변경 내역을 기록하므로, 이전 상태로 되돌아갈 수 있습니다.

#### 예시

1. `git reflog`를 사용하여 참조 로그를 확인:

    ```bash
    git reflog
    ```

2. 복구하려는 커밋의 해시를 찾은 후, 해당 커밋으로 되돌리기:

    ```bash
    git reset --hard <commit-hash>
    ```

이렇게 하면 실수로 삭제한 커밋을 복구할 수 있습니다.

`git reset` 명령어는 매우 강력하지만, 잘못 사용하면 데이터 손실이 발생할 수 있으므로 주의해서 사용해야 합니다.