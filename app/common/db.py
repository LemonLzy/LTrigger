import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# 从环境变量中获取用户名
def get_username():
    return os.environ.get("L_TRIGGER_USERNAME")


# 从环境变量中获取密码
def get_password():
    return os.environ.get("L_TRIGGER_PASSWORD")


# 从环境变量中获取数据库地址+端口
def get_host():
    return os.environ.get("L_TRIGGER_HOST")


# 从环境变量中获取数据库名
def get_database():
    return os.environ.get("L_TRIGGER_DATABASE")


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{get_username()}:{get_password()}@{get_host()}/{get_database()}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == '__main__':
    print(get_username())
