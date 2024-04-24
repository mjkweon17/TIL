## 윈도우

### 프로젝트 구조 추출
- 루트 디렉토리에서 `tree /f /a`
    - 모든 디렉토리와 파일을 ASCII 형식으로 표시
    - /f: 파일을 포함하라
    - /a: ASCII 문자만 사용하라

### icals
- Windows 운영 체제에서 파일과 폴더의 권한을 관리하는 명령줄 도구
- Integrity Control Access Control Lists의 약자
- 다음과 같은  작업 수행 가능
    - 파일이나 폴더의 현재 권한 표시
    - 사용자나 그룹에 대한 권한 부여, 거부 또는 제거
    - 권한 상속 설정 또는 제거
    - 파일이나 폴더의 소유자 변경
- 권한 플래그
    - (I) - Inheritance (상속)
        - 이 플래그는 해당 권한이 상위 폴더로부터 상속되었음을 나타냄.
        - 상속된 권한은 상위 폴더의 권한 설정에 따라 자동으로 적용됨.
    - (M) - Modify (수정)
        - 이 플래그는 해당 사용자나 그룹이 파일 또는 폴더를 수정할 수 있는 권한을 가지고 있음을 나타냄.
        - 수정 권한에는 파일 내용 변경, 파일 삭제, 파일 이름 변경 등이 포함됨.
    - (F) - Full Access (모든 권한)
        - 이 플래그는 해당 사용자나 그룹이 파일 또는 폴더에 대한 모든 권한을 가지고 있음을 나타냄.
        - 모든 권한에는 읽기, 쓰기, 실행, 삭제, 권한 변경 등이 포함됨.
    - 그 외 다양한 권한 플래그
        (R) - Read (읽기)
        (W) - Write (쓰기)
        (X) - Execute (실행)
        (D) - Delete (삭제)
        (P) - Change Permissions (권한 변경)
        (O) - Take Ownership (소유권 가져오기)
    - 이러한 권한 플래그를 조합하여 사용자나 그룹에 특정 권한을 부여하거나 제거할 수 잇음. icacls 명령을 사용할 때는 필요한 권한만 부여하고, 불필요한 권한은 제거하는 것이 보안상 좋은 방법.

### ssh 접속
- ssh ubuntu@210.109.52.43 -p 22
- ssh -i C:\Users\explo\Desktop\kubook-backend\src\kucc-lib-key1.pem ubuntu@210.109.53.23 -p 22

- ssh -i <keyfile_path> <username>@<host> -p <port>
    - 아래와 같은 에러 메시지 발생
        ```bash
        Bad permissions. Try removing permissions for user: BUILTIN\\Users (S-1-5-32-545) on file C:/Users/explo/Desktop/kubook-backend/src/kucc-lib-key1.pem.
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        Permissions for 'C:\\Users\\explo\\Desktop\\kubook-backend\\src\\kucc-lib-key1.pem' are too open.
        It is required that your private key files are NOT accessible by others.
        This private key will be ignored.
        Load key "C:\\Users\\explo\\Desktop\\kubook-backend\\src\\kucc-lib-key1.pem": bad permissions
        ubuntu@210.109.53.23: Permission denied (publickey).
        ```
    - 개인 키 파일은 다른 사용자나 그룹이 접근할 수 없도록 보호되어야 하는데, SSH 키 파일의 권한이 너무 개방적으로 설정되어 있어서 발생한 에러. 이 문제를 해결하려면  SSH 키 파일(kucc-lib-key1.pem)의 권한을 올바르게 설정해서, 소유자(현재 사용자)만 읽을 수 있어야 하며, 다른 사용자나 그룹의 접근을 제한해야 함.
    - BUILTIN\Users: Windows 운영 체제에 기본적으로 존재하는 로컬 그룹 중 하나. 이 그룹은 로컬 컴퓨터에 로그온한 모든 사용자를 포함.