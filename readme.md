# MOCI DdaSoop File BE


## 🧐 프로젝트 소개

파일 업로드를 담당하는 백엔드 서버입니다.

서버 내부에서만 사용할 예정입니다.

## 🚀 시작하기

### 전제 조건

- Docker

### 설치 및 실행

1.  **Docker 이미지 빌드**

    ```shell
    docker build -t moci-ddasoop-file-be .
    ```

2.  **Docker 컨테이너 실행**

    ```shell
    docker run -v uploads:/app/uploads -p 8080:8000 --name moci-ddasoop-file-be moci-ddasoop-file-be
    ```

## 📖 API 엔드포인트

### `POST /file/upload`

-   **설명:** 파일을 업로드합니다.
-   **요청:**
    -   `file`: 업로드할 파일 (multipart/form-data)
-   **응답:**
    -   `200 OK`: 파일 업로드 성공
        ```json
        {
          "file_url": "string",
          "file_name": "string",
          "content_type": "string",
          "size": "integer"
        }
        ```
    -   `404 Not Found`: 파일을 찾을 수 없음

## 📁 프로젝트 구조

```
MOCI-ddassop/backend/MOCI_DdaSoop_File_BE/
├───.env.default
├───.gitignore
├───Dockerfile
├───pyproject.toml
├───readme.md
├───uv.lock
├───.github/
│   ├───PULL_REQUEST_TEMPLATE.md
│   ├───ISSUE_TEMPLATE/
│   │   ├───chore.md
│   │   ├───docs.md
│   │   ├───feature.md
│   │   ├───fix.md
│   │   ├───perf.md
│   │   ├───refactor.md
│   │   ├───style.md
│   │   └───test.md
│   └───workflows/
│       ├───file_backend_cd.yml
│       └───file_backend_ci.yml
├───src/
│   ├───main.py
│   ├───common/
│   │   ├───database/
│   │   │   └───database.py
│   │   └───env/
│   │       ├───config.py
│   │       └───env.py
│   ├───domain/
│   │   ├───__pycache__/
│   │   └───file/
│   │       ├───controller/
│   │       │   ├───file_route.py
│   │       │   └───__pycache__/
│   │       ├───dto/
│   │       │   ├───FileCreateDTO.py
│   │       │   └───FileInfoDTO.py
│   │       └───entity/
│   │           ├───File.py
│   └───tests/
│       └───__init__.py
└───uploads/...
```