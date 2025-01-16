# Git 레퍼지토리 로컬 생성 및 GitHub 서버에 커밋 및 푸시

## 1. 로컬 레퍼지토리 생성
```bash
# Git 초기화
git init
```

## 2. GitHub에 새로운 레퍼지토리 생성
1. GitHub 웹사이트에 로그인합니다.
2. 오른쪽 상단의 `+` 버튼을 클릭하고 `New repository`를 선택합니다.
3. 레퍼지토리 이름을 입력하고 `Create repository` 버튼을 클릭합니다.

## 3. 로컬 레퍼지토리를 GitHub 레퍼지토리와 연결
```bash
# 원격 레퍼지토리 추가
git remote add origin https://github.com/{username}/git-test.git
# 브랜치 이름 변경
git branch -M master
```

## 4. 커밋
```bash
# 커밋
git commit -m "b-funtion.txt"
```

## 5. GitHub 서버에 푸시
```bash
# 처음 푸시
git push -u origin master
# -u: 서버의 원격 저장소가 비어있는 경우, 한 번만 할 수 있음

# 추후에 팀원과 공유시에는 한사람이 첫 push를 실행하고(원격 저장소 생성)
# 다른 팀원들은 서버에서 clone 하여 사용

# 이후 푸시
git push

```

## 6. 브랜치 관련 명령어

 * 브랜치란?<br>
브랜치(Branch)는 버전 관리 시스템에서 코드의 독립적인 작업 흐름을 나타내는 개념입니다.<br>
주로 새로운 기능을 개발하거나 버그를 수정할 때 사용되며, <br>
메인 코드베이스와 분리된 상태에서 작업을 진행할 수 있습니다.<br>
작업이 완료되면 브랜치를 메인 코드베이스에 병합(Merge)하여 변경 사항을 반영합니다.

### 브랜치 이름 변경
```bash
# 브랜치 이름 변경
git branch -M <branch-name>
```

### 브랜치 생성
```bash
# 브랜치 생성
git branch <branch-name>
```

### 브랜치 목록 확인
```bash
# 브랜치 목록 확인
git branch
```

### 브랜치 전환
```bash
# 브랜치 전환
git checkout <branch-name>
```

### 브랜치 생성 및 전환
```bash
# 브랜치 생성 및 전환
git checkout -b <branch-name>
```

### 브랜치 삭제
```bash
# 브랜치 삭제
git branch -d <branch-name>
```

### 원격 브랜치 삭제
```bash
# 원격 브랜치 삭제
git push origin --delete <branch-name>
```

## 7. 클론

### 클론이란?
클론(Clone)은 원격 저장소의 전체 내용을 로컬 컴퓨터에 복사하는 작업입니다. 이를 통해 원격 저장소의 파일과 폴더를 로컬에서 동일하게 사용할 수 있습니다.

### 클론 명령어
```bash
# 클론
git clone <githubURL> <FolderName>
# <FolderName>이 없는 경우, 서버 레퍼지토리의 이름을 가진 폴더안에 저장소가 클론됩니다.
```

### 사용 예시
```bash
# 예시: 특정 GitHub 저장소를 'git-clone' 폴더에 클론
git clone https://github.com/{username}/git-test.git git-clone
```

### 클론 후 작업
클론 후에는 로컬 저장소에서 브랜치를 전환하거나 파일을 수정하고 커밋한 후, 변경 사항을 원격 저장소에 푸시할 수 있습니다.

## 8. git checkout 사용 방법
HEAD를 이동시키는 명령어

### 기존 브랜치로 전환
```bash
# 기존 브랜치로 전환
git checkout <branch-name>
```
`<branch-name>`을 전환하고자 하는 브랜치 이름으로 변경합니다.

### 새로운 브랜치 생성 및 전환
```bash
# 새로운 브랜치 생성 및 전환
git checkout -b <new-branch-name>
```
`<new-branch-name>`을 생성하고자 하는 브랜치 이름으로 변경합니다.
### 특정 커밋 시점으로 돌아가기
```bash
# 특정 커밋 시점으로 돌아가기
git checkout <commit-hash>
```
`<commit-hash>`를 돌아가고자 하는 커밋의 해시 값으로 변경합니다. 이 명령어를 실행하면 해당 커밋 시점의 파일 상태로 워킹 디렉토리가 변경됩니다.

## HEAD란?
`HEAD`는 현재 체크아웃된 커밋 또는 브랜치를 가리키는 포인터입니다. 보통 현재 작업 중인 브랜치를 가리키며, 브랜치를 전환하거나 특정 커밋으로 이동할 때 업데이트됩니다.

예를 들어:
- `git checkout <branch-name>` 명령어를 사용하면 `HEAD`가 해당 브랜치를 가리킵니다.
- `git checkout <commit-hash>` 명령어를 사용하면 `HEAD`가 해당 커밋을 가리킵니다.