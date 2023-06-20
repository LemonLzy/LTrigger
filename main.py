from fastapi import FastAPI

from app.conf.conf import init_env

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event("startup")
async def startup_event():
    # 由于os.environ设置的环境变量的生命周期与当前进程的生命周期相同，当 FastAPI 项目停止时，这些环境变量将自动被销毁
    init_env()
    print("项目启动，已设置环境变量")
