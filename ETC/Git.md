### git log
- git log
    - 모든 커밋 히스토리  나열
- git log -n <limit>
    - 최근 n개의 커밋을 보여줌
    - git log -n 3를 쓰면 최근 3개의 커밋을 보여줌
- git log --oneline
    - 각 커밋을 한 줄로 요약해서 보여줌. 커밋 ID의 앞부분과 커밋 메시지만 포함됨
- git log --graph
    - 커밋 히스토리를 ASCII 그래프로 보여줌. 브랜치와 머지 히스토리를 시각적으로 확인할 수 있음
- git log --author="<author>"
    - 특정 저자의 커밋만을 필터링해서 보여줌. 여기서 <author>에는 저자의 이름이나 이메일의 일부를 넣을 수 있음.
- git log <filt_path>
    - 특정 파일의 커밋 히스토리 확인하기

### 커밋 변경 사항 확인하기
    - git show <commit_id>

### 커밋 취소
- git reset
    - 현재 HEAD를 이전 커밋으로 옮기는데 사용
    - 작업 디렉토리의 변경 사항을 유지하면서 마지막 커밋을 '취소'할 수 있음
    - 주로 3가지 옵션이 사용됨: --soft, --mixed, --hard
    - 가장 안전한 방법은 --soft 옵션을 사용하는 것
- git reset --soft Head~1
    - 가장 마지막 커밋을 취소하고, 해당 커밋의 변경 사항들을 스테이징 영역에 유지
- git reset --hard
    - 커밋된 변경 사항을 완전히 제거
    - 주의해서 사용해야 함
- git reset --hard HEAD~1
    - 가장 마지막 커밋을 취소하고, 해당 커밋의 변경 사항들을 작업 디렉토리에서도 제거

- git revert
    - 특정 커밋의 변경 사항을 취소하는 새로운 커밋을 생성
    - 커밋 히스토리를 유지하면서 변경 사항만을 취소하고 싶을 때 유용
- git revert HEAD
    - 가장 마지막 커밋을 취소하는 새로운 커밋을 생성
        - 변경 사항을 되돌리지만, 원래 커밋은 히스토리에 남아 있음

### 로컬 Git 저장소에서 GitHub에 새로 만든 브랜치로 전환하기
1. 터미널이나 Git Bash를 열고 프로젝트 디렉토리로 이동
2. 현재 브랜치를 확인하려면 다음 명령을 실행:
   ```
   git branch
   ```
   이 명령은 로컬 저장소의 모든 브랜치를 나열하고 현재 브랜치 앞에는 별표(*)가 표시됨.
3. GitHub에서 만든 브랜치를 로컬 저장소로 가져오기 위해 다음 명령을 실행함
    ```bash
    # 원격 저장소(origin)에서 최신 변경 사항을 가져옴.
    git fetch origin 
    # 현재 branch에서 최신 변경사항을 모두 가져오고, 변경사항을 업데이트
    git fetch --all
    ```
4. 이제 GitHub에서 만든 브랜치로 전환할 수 있음. 브랜치 이름이 `feature/github-actions-ci-cd`라고 가정할 때 다음 명령을 실행함
   ```
   git checkout feature/github-actions-ci-cd
   ```
   이 명령은 지정된 브랜치로 전환합니다. 브랜치가 로컬에 존재하지 않으면 원격 브랜치를 기반으로 새 로컬 브랜치를 생성함.
5. 브랜치가 성공적으로 전환되었는지 확인하려면 다시 `git branch` 명령을 실행.
6. 변경 사항을 GitHub의 해당 브랜치에 푸시하려면 다음 명령을 사용합니다:
    ```
    git push origin feature/github-actions-ci-cd
    ```
    이 명령은 로컬 브랜치의 변경 사항을 GitHub의 동일한 이름의 브랜치에 푸시

### 새로운 브랜치 만들기
1. 터미널을 열고 Git 저장소로 이동합니다.
    ```
    cd /path/to/your/repo
    ```
2. 현재 브랜치를 확인합니다.
    ```
    git branch
    ```
3. 새로운 브랜치를 생성합니다.
    ```
    git branch new-branch-name
    ```
4. 새로 생성한 브랜치로 전환합니다.
    ```
    git checkout new-branch-name
    ```
5. 원격 저장소에 새 브랜치를 푸시합니다.
    ```
    git push -u origin new-branch-name
    ```

- 3번과 4번 과정을 한 번에 할 수 있는 단축 명령어
    ```
    git checkout -b new-branch-name
    ```
    - 이 명령어는 새 브랜치를 생성하고 바로 전환까지 해줌.

### 현재 작업 중인 브랜치 삭제하기
- 현재 작업 중인 브랜치를 삭제하려면, 먼저 다른 브랜치로 전환해야 함. 삭제할 브랜치에서는 삭제 작업을 할 수 없기 때문.

1. 삭제할 브랜치가 아닌 다른 브랜치로 전환합니다. 일반적으로 main 브랜치로 전환함.
    ```
    git checkout main
    ```
2. 삭제할 브랜치를 확인함.
    ```
    git branch
    ```
3. 로컬 브랜치를 삭제함.
    ```
    git branch -d branch-to-delete
    ```
    만약 브랜치에 머지되지 않은 변경 사항이 있다면, Git은 경고 메시지를 표시하고 삭제를 진행하지 않음. 이 경우, 강제로 삭제하려면 `-D` 옵션을 사용.
    ```
    git branch -D branch-to-delete
    ```
4. 원격 저장소에서도 브랜치를 삭제하려면 다음 명령어를 사용.
    ```
    git push origin --delete branch-to-delete
    ```
    이렇게 하면 로컬과 원격 저장소 모두에서 브랜치가 삭제됩니다.
- 주의: 브랜치를 삭제하면 해당 브랜치에서의 작업 내용이 모두 사라지므로, 필요한 변경 사항은 미리 다른 브랜치에 머지하는 것이 좋음. 삭제 전에는 꼭 브랜치의 상태를 확인해야 함.

### publish branch
- VS Code의 Git 기능을 사용할 때, 새로운 브랜치를 만들고 커밋했지만 `git push -u origin new-branch-name` 명령을 실행하지 않았다면, VS Code는 "Publish Branch"라는 옵션을 표시함.
- "Publish Branch"는 VS Code에서 제공하는 기능으로, 아직 원격 저장소에 푸시되지 않은 로컬 브랜치를 원격 저장소에 푸시할 수 있게 해줌. 이 기능은 essentially `git push -u origin new-branch-name` 명령과 동일한 작업을 수행함.
- 따라서 "Publish Branch"를 클릭하면, VS Code는 현재 브랜치를 원격 저장소에 푸시하고, 로컬 브랜치와 원격 브랜치를 연결함. 이후에는 `git push`나 `git pull` 명령을 사용할 때 브랜치 이름을 명시하지 않아도 됨.
- 이는 VS Code가 제공하는 편의 기능 중 하나로, Git 명령을 직접 입력하지 않고도 쉽게 원격 저장소와 상호 작용할 수 있도록 도와줌. 하지만 이 기능은 Git의 기본 기능을 대체하는 것은 아니므로, 터미널에서 Git 명령을 직접 사용할 수도 있음.

### 원격 저장소
- remote repository
- Git을 사용할 때 로컬 컴퓨터 외부에 있는 Git 저장소를 의미
- 주요 특징
    - 공동 작업: 원격 저장소를 통해 여러 사람이 동시에 프로젝트에 참여할 수 있음
    - 백업 및 복구: 로컬 컴퓨터의 데이터가 손실되더라도 원격 저장소에 저장된 프로젝트 데이터를 복구할 수 있음
    - 버전 관리: 원격 저장소에 프로젝트 변경 내역이 기록되어 버전 관리가 가능함
    - 다양한 환경에서의 접근: 네트워크에 접속할 수 있다면 어디에서든 원격 저장소에 접근할 수 있음
    - 협업 및 배포: 팀원 간 코드 공유 및 배포가 편리함
- 일반적으로 원격 저장소는 GitHub, GitLab, Bitbucket과 같은 온라인 호스팅 서비스에 저장되며, SSH, HTTPS 등의 프로토콜을 통해 접근할 수 있음

### git push branch-name vs git push origin branch-name 
- GitHub에 브랜치를 푸시할 때는 일반적으로 git push origin branch-name을 사용하는 것이 더 좋음
- 명시적인 원격 저장소 지정: git push origin branch-name은 명시적으로 origin이라는 원격 저장소를 지정하여 푸시함. 이는 원격 저장소 설정이 복잡한 경우에도 안전하게 동작할 수 있음.
- GitHub 연결 시 자동 설정: GitHub에 저장소를 처음 클론하거나 연결할 때, 원격 저장소 이름이 자동으로 origin으로 설정됨. 따라서 git push origin branch-name이 가장 일반적인 명령어임.
- 가독성과 명확성: git push origin branch-name이 어떤 원격 저장소에 푸시하는지 명확하게 보여줌. git push branch-name만으로는 어느 원격 저장소에 푸시하는지 불분명할 수 있음.

### git filter-branch -f --index-filter "git rm --cached --ignore-unmatch [파일명]" --prune-empty -- --all
- 특정 파일을 리포지토리의 커밋 히스토리에서 완전히 제거
- git filter-branch
    - Git 저장소의 커밋 히스토리를 필터링하고 다시 작성할 때 사용
    - 기존의 커밋들을 수정하거나, 특정 조건에 맞는 커밋들을 완전히 제거할 수 있음
- -f
    - git filter-branch 명령의 안전 장치를 무시하고 강제로 실행하게 함
    - 기본적으로, Git은 이미 filter-branch가 적용된 리포지토리에 대해 재실행을 막으려 할 때 경고를 보냄
    - 이 옵션을 사용하면 해당 경고를 무시하고 명령을 실행함
- --index-filter:
    - 각 커밋의 인덱스(스테이징 영역)에 필터를 적용함
    - 스크립트("git rm --cached --ignore-unmatch [파일명]")는 지정된 파일을 각 커밋에서 제거함
- "git rm --cached --ignore-unmatch [파일명]"
    - git rm --cached: 파일을 인덱스에서 제거하지만, 작업 디렉토리에는 파일을 유지
    - --ignore-unmatch: 지정된 파일이 존재하지 않아도 오류를 발생시키지 않고 명령을 계속 진행함
- --prune-empty:
    - 변경 사항이 없는 (즉, 빈) 커밋들을 히스토리에서 제거. 파일 제거로 인해 변경 사항이 없는 커밋은 이 옵션에 의해 삭제됨.
-- --all:
    - 이 명령어는 모든 브랜치와 태그에 대해 필터를 적용. --all은 리포지토리의 모든 참조(브랜치, 태그 등)를 대상으로 함.

### git filter-branch --tree-filter 'find . -type f -exec sed -i "s/FIREBASE_WEB_API_KEY = \"asdf\"/FIREBASE_WEB_API_KEY = \"\"/g" {} +' HEAD
- `git filter-branch`를 사용하여 특정 코드 줄이 포함된 모든 파일의 내용을 변경하는 작업은 다음과 같이 수행할 수 있음
- `--tree-filter`: 각 커밋에 대해 지정된 명령을 실행하고, 결과를 새 커밋으로 기록함.
- `find . -type f`: 현재 디렉토리(및 하위 모든 디렉토리)에서 모든 파일을 찾음.
- `-exec`: 찾은 각 파일에 대해 뒤따르는 `sed` 명령을 실행함.
- `sed -i`: 파일을 직접 수정하도록 sed에 지시함. (`-i`는 in-place 수정을 의미함.)
- `s/FIREBASE_WEB_API_KEY = "asdf"/FIREBASE_WEB_API_KEY = ""/g`: 주어진 패턴을 찾아서 빈 문자열로 대체
- `HEAD`: 현재 체크아웃된 브랜치의 HEAD 부터 필터를 적용

### 브랜치 naming convention
- `feature`나 `bugfix` 같은 키워드는 브랜치의 카테고리를 나타내며, 일반적으로 이 키워드 다음에 오는 `/` 는 해당 카테고리에 속하는 하위 브랜치를 생성할 때 사용됨. 즉, `feature` 나 `bugfix` 자체를 하나의 브랜치로 사용하기보다는, 이들을 브랜치의 분류로 사용하고, 실제 작업을 위한 브랜치는 이들 카테고리 아래에 추가적으로 파게 됨.
    - 예시
        - `feature/login`: 이는 `feature` 카테고리에 속하며, "login" 기능을 개발하기 위한 브랜치.
        - `bugfix/login-error`: 이는 `bugfix` 카테고리에 속하며, "login" 관련 오류를 수정하기 위한 브랜치.
- 각 브랜치는 특정 작업이나 기능의 개발을 목적으로 생성되며, 브랜치 이름에 카테고리를 포함시키는 것은 그 브랜치의 목적이나 종류를 더 명확하게 표현하기 위함. 따라서 `feature`, `bugfix` 등을 사용할 때는 그 아래 구체적인 작업 내용을 나타내는 하위 브랜치를 추가로 생성하는 것이 일반적인 사용 방법.
