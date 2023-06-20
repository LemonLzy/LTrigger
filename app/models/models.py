from sqlalchemy import Column, Integer, String, DATETIME, TIMESTAMP, sql
from sqlalchemy.sql import func

from app.common.db import Base


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    desc = Column(String(255))
    ip_address = Column(String(255))
    database = Column(String(255))
    port = Column(Integer)
    user = Column(String(255))
    password = Column(String(255))
    status = Column(Integer)
    create_name = Column(String(255))
    update_name = Column(String(255))
    create_time = Column(DATETIME, server_default=sql.func.now())
    lastUpdate_time = Column(DATETIME, server_default=sql.func.now())


class Directory(Base):
    __tablename__ = "directory"
    id = Column(Integer, primary_key=True, index=True)
    tab_name = Column(String(255))
    parent_id = Column(Integer)  # 父节点id
    type = Column(Integer)  # 节点类型，0表示目录，1表示节点
    display = Column(Integer)  # 是否展示，1为展示，0不展示，默认为1


class DataScript(Base):
    __tablename__ = "datascript"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer)
    script = Column(String)


class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(Integer)
    page = Column(String)
    create_time = Column(TIMESTAMP, default=func.now())
