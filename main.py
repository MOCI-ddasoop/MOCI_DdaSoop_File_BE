from fastapi import FastAPI
from domain.file import router as FileRouter

app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(FileRouter)