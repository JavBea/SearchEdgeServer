from flask import Flask
from flask_cors import CORS
import sys

import src.config.config as config
from src.blueprints.llm_bp import llm_bp
import pymysql

from src.blueprints.login_bp import login_bp
from src.blueprints.register_bp import register_bp
from src.services.dbService import db

# 设置整个项目的默认编码模式为“utf-8”
sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)

# 需要在应用上下文中执行的代码
with app.app_context():
    # 此处的代码以安全地访问 Flask 配置与数据库
    pymysql.install_as_MySQLdb()
    print("App context is active")

# pymysql.install_as_MySQLdb()
# 导入数据库配置文件至flask对象
app.config.from_object(config)
# 初始化一个SQLAlchemy对象
db.init_app(app)

# 测试数据库连接是否成功（create_all将定义的所有表类映射为数据库下的表）
with app.app_context():
    # 在这里进行数据库操作
    db.create_all()  # 创建所有表

# 配置 CORS（允许跨域访问）
# 只允许 localhost 的所有端口访问
CORS(app, resources={r"/*": {"origins": r"http://localhost:\d+"}})

app.register_blueprint(llm_bp, url_prefix='/llm')
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

@app.route('/')
def hello_world():  # put application's code here

    from src.config.apis import GPT_API
    from src.config.apis import QWEN_API
    from src.config.apis import GOOGLE_CSE_API
    from src.config.apis import GOOGLE_CSE_CX
    print("this GPT_API: " + GPT_API)
    print("this QWEN_API: " + QWEN_API)
    print("this Google_API: " + GOOGLE_CSE_API)
    print("this Google_CX: " + GOOGLE_CSE_CX)

    return 'Hello You!'


@app.before_request
def initialize():
    """
    首次访问服务器前，访问数据库，更新src/config/apis.py中的各个API
    然后初始化大模型客户端与搜索方法
    :return:
    """
    from src.config import apis
    if not apis.INIT_FLAG:
        from src.services.modelServices.ApiService import ApiService
        ApiService.update_api_file()
        apis.INIT_FLAG = True

    # 初始化大模型访问客户端
    from src.services.llmService import llm_client_init
    llm_client_init()

    # 初始化搜索引擎访问方法
    from src.services.searchService import search_client_init
    search_client_init()


if __name__ == '__main__':
    app.run()
