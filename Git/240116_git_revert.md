# Git Revert

`git revert` 명령어는 Git에서 특정 커밋을 되돌리는 데 사용됩니다.<br>
이 명령어는 기존의 커밋을 취소하는 새로운 커밋을 생성하여, 히스토리를 보존하면서 변경 사항을 되돌립니다.<br>
특정 커밋을 무효화 하고 새로운 커밋을 만들지만, 이전 커밋은 남아있어서 접근이 가능합니다.<br>

## 사용법

```sh
git revert <commit-hash>
```

- `<commit-hash>`: 되돌리고자 하는 커밋의 해시 값입니다.

## 추가 옵션

### `--no-edit` 옵션

`--no-edit` 옵션을 사용하면, revert 커밋 메시지를 편집하지 않고 기본 메시지를 그대로 사용합니다.

```sh
git revert <commit-hash> --no-edit
```

### `--no-commit` 옵션

`--no-commit` 옵션을 사용하면, revert 작업을 수행하지만 자동으로 커밋하지 않습니다. 이 옵션을 사용하면 변경 사항을 검토하고 수동으로 커밋할 수 있습니다.

```sh
git revert <commit-hash> --no-commit
```

## 예시

1. 특정 커밋을 되돌리기:

    ```sh
    git revert abc1234
    ```

2. 여러 커밋을 순차적으로 되돌리기:

    ```sh
    git revert abc1234 def5678
    ```


## 주의사항

- `git revert`는 되돌린 커밋을 새로운 커밋으로 추가하기 때문에, 히스토리가 보존됩니다.
- 되돌린 커밋이 다른 커밋에 영향을 미칠 수 있으므로, 되돌리기 전에 충분히 검토해야 합니다.

## 참고 자료

- [Git 공식 문서 - git revert](https://git-scm.com/docs/git-revert)
- [Atlassian Git Tutorial - Revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)
