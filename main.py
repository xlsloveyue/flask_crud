"""
Created by ranml on 2019/1/28
"""
from app import create_app

__author__ = 'ranml'

# 创建 app ，定义在 app/__init__.py
app = create_app()

# 配置文件中的 debug，定义在 config/app.py
debug = app.config['DEBUG']

# print(debug)
if __name__ == "__main__":
    # app.config["SQLALCHEMY_ECHO"] = True
    app.run(debug=debug, host='127.0.0.1', port=8002)
