# MOCI DdaSoop File BE


## 🧐 프로젝트 소개

파일 업로드를 담당하는 백엔드 서버입니다.

서버 내부에서만 사용할 예정입니다.

## 문서 페이지
`http://localhost:8000/docs`

## 🚀 시작하기

### 전제 조건

- Docker
- uv

### 설치 및 실행

0. **Python 경로 설정**
    ```shell
    source set_python_path.sh
    ```

1.  **로컬에서 실행**
    ```shell
    pip install uv
    uv run uvicorn main:app --reload --port 8000
    ```

2.  **Docker로 실행**

    a. **Docker 이미지 빌드**
    ```shell
    docker build -t moci-ddasoop-file-be .
    ```

    b. **Docker 컨테이너 실행**
    ```shell
    docker run -v ./uploads:/app/uploads -p 8000:8000 --name moci-ddasoop-file-be moci-ddasoop-file-be
    ```

   3. **docker-compose로 실행**
   
    a. **실행**
    ```shell
    docker-compose up -d
    ```
## 📖 API 엔드포인트

### `POST /file/url`

-   **설명:** 파일 업로드에 사용할 URL을 생성합니다. (현재 구현은 로컬 호스트 URL을 반환합니다.)
-   **응답:**
    -   `200 OK`: `{ "file_url": "http://localhost:8000/file" }`

### `GET /file/url`

-   **설명:** 저장된 파일의 URL을 가져옵니다.
-   **요청:**
    -   `file_name` (쿼리 파라미터): 가져올 파일의 이름
-   **응답:**
    -   `200 OK`: `{ "file_url": "http://localhost:8000/uploads/{file_name}" }`
    -   `404 Not Found`: 파일을 찾을 수 없음

### `POST /file/`

-   **설명:** 파일을 업로드합니다.
-   **요청:**
    -   `file`: 업로드할 파일 (multipart/form-data)
-   **응답:**
    -   `200 OK`

### `DELETE /file/{file_name}`

-   **설명:** 지정된 파일을 삭제합니다.
-   **요청:**
    -   `file_name` (경로 파라미터): 삭제할 파일의 이름
-   **응답:**
    -   `200 OK`
    -   `404 Not Found`: 파일을 찾을 수 없음

## 📁 프로젝트 구조

```
MOCI-ddassop/backend/MOCI_DdaSoop_File_BE/
├───.env.default
├───.gitignore
├───alembic.ini
├───Dockerfile
├───pyproject.toml
├───readme.md
├───set_python_path.sh
├───test_main.http
├───uv.lock
├───.github/
│   └───...
├───src/
│   ├───__init__.py
│   ├───main.py
│   ├───common/
│   │   ├───dependency_injector/
│   │   │   └───container.py
│   │   └───env/
│   │       ├───config.py
│   │       ├───env.py
│   │       └───profile/
│   │           ├───BaseProfileConfig.py
│   │           ├───DevProfileConfig.py
│   │           ├───ProdProfileConfig.py
│   │           └───TestProfileConfig.py
│   ├───domain/
│   │   ├───file/
│   │   │   ├───controller/
│   │   │   │   └───file_controller.py
│   │   │   ├───dto/
│   │   │   │   ├───FileInfoDTO.py
│   │   │   │   └───ImageFileSizeDTO.py
│   │   │   └───service/
│   │   │       └───file_service.py
│   │   └───home/
│   │       └───controller/
│   │           └───home_router.py
│   └───tests/
│       ├───domain/
│       │   └───file/
│       │       └───controller/
│       │           └───test_file_route.py
│       └───resources/
│           └───sample.jpg
└───uploads/...
```