from flask import Flask
from src.blueprints.llm_bp import llm_bp
from flask_cors import CORS
import sys


# 设置整个项目的默认编码模式为“utf-8”
sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)

# 配置 CORS（允许跨域访问）
# 只允许 localhost 的所有端口访问
CORS(app, resources={r"/*": {"origins": r"http://localhost:\d+"}})

app.register_blueprint(llm_bp, url_prefix='/llm')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello You!'


if __name__ == '__main__':
    app.run()
