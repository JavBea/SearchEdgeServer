from flask import Flask
from app.blueprints.llm_bp import llm_bp

app = Flask(__name__)

app.register_blueprint(llm_bp, url_prefix='/llm')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
