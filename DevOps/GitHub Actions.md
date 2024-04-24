### &{{}}처럼 괄호를 두 개 겹치는 이유
- 괄호 안의 값을 변수로 취급하기 위해. 만약 괄호를 한 개만 겹치면 괄호 안의 값을 문자열로 취급함.

### docker/login-action@v1
```yml
    - name: Login to Kakao Cloud Container Registry
      uses: docker/login-action@v1
      with:
        registry: ${{ secrets.KAKAO_CLOUD_PROJECT_NAME }}.kr-central-2.kcr.dev
        username: ${{ secrets.KAKAO_CLOUD_ACCESS_KEY }}
        password: ${{ secrets.KAKAO_CLOUD_ACCESS_SECRET_KEY }}
    - name: Build and push docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        file: ./Dockerfile
        push: true
        tags: ${{ secrets.KAKAO_CLOUD_PROJECT_NAME }}.kr-central-2.kcr.dev/${{ secrets.KAKAO_CLOUD_REPOSITORY_NAME }}/lifebook:latest
```
- context
    - Docker 이미지를 빌드할 때 사용되는 작업 디렉토리나 소스 코드의 위치
    - Docker 빌드 과정에서 context로 지정된 디렉토리 내의 파일들은 Docker 데몬으로 전송되며, Dockerfile 내에서 참조될 수 있음
    - `.`은 현재 디렉토리은 의미. Docker 빌드 커맨드가 실행되는 위치와 동일한 디렉토리가 빌드 컨텍스트로 사용됨. Dockerfile과 프로젝트의 소스 코드가 현재 디렉토리 내에 위치하고 있음을 가정함.
    - context 없이 Docker 이미지르 ㄹ빌드하는 것은 기술적으로 가능하지 않음
    - Docker 이미지 빌드 시, 반드시 어떤 컨텍스트(소스 코드와 리소스가 있는 디렉토리)를 사용할 것인지 지정해야 함
    - CLI에서 Docker 이미지를 빌드할 때 context를 명시적으로 지정하지 않으면, 기본적으로 현재 작업 디렉토리(.)가 사용됨. 그러나, Docker 빌드 액션 같은 CI/CD 파이프라인 도구에서는 이 값을 명시적으로 설정해야 할 수 있음.
- file
    - 사용할 Dockerfile의 경로와 파일명을 지정
    - file 지시어는 선택적
    - file 지시어를 생략하면, Docker는 기본적으로 컨텍스트 디렉토리의 Dockerfile이라는 이름의 파일을 찾아서 사용. 만약 루트 디렉토리에 Dockerfile이 있고, 특별한 설정 없이 기본 Dockerfile을 사용하려는 경우 file 지시어 없이 빌드를 진행할 수 있음.
    