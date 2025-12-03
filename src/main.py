from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from domain.file.controller import router as file_router
from domain.home.controller import router as home_router
from common.dependency_injector import Container

def create_app() -> FastAPI:
    app = FastAPI(
        title="File API",
        docs_url="/docs",
        redoc_url=None,
    )
    container = Container()

    container.wire(
        modules=container.wiring_config.modules,
        packages=container.wiring_config.packages
    )
    app.container = container

    app.mount("/files", StaticFiles(directory="uploads"), name="files")

    app.include_router(file_router)
    app.include_router(home_router)

    origins = [
        "http://localhost:3000",
        "http://localhost:8000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
app = create_app()