import toml
import os

# 设置默认值
default_config = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'LTrigger',
        'password': 'LTrigger',
        'db_name': 'LTrigger',
        'max_open_conns': 10,
        'max_idle_conns': 200,
        'migrate_table': True,
    }
}


def init_env():
    try:
        with open('./app/conf/conf.toml', 'r') as f:
            config = toml.load(f)
    except FileNotFoundError:
        print("配置文件不存在")
    except toml.TomlDecodeError:
        print("配置文件格式不正确")
    except KeyError as e:
        print(f"配置文件错误：{e}")
    else:
        # 获取配置信息，并设置默认值
        db_config = config.get('db', {})
        for key in default_config['db']:
            db_config[key] = db_config.get(key, default_config['db'][key])

    # 设置环境变量
    os.environ['LTRIGGER_DB_HOST'] = config['db']['host']
    os.environ['LTRIGGER_DB_PORT'] = str(config['db']['port'])
    os.environ['LTRIGGER_DB_USER'] = config['db']['user']
    os.environ['LTRIGGER_DB_PASSWORD'] = config['db']['password']
    os.environ['LTRIGGER_DB_NAME'] = config['db']['db_name']
    os.environ['LTRIGGER_DB_MAX_OPEN_CONNS'] = str(config['db']['max_open_conns'])
    os.environ['LTRIGGER_DB_MAX_IDLE_CONNS'] = str(config['db']['max_idle_conns'])
    os.environ['LTRIGGER_DB_MIGRATE_TABLE'] = str(config['db']['migrate_table'])
