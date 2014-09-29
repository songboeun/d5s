#-*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


'''
주소 추가방법을 설명합니다!

@app.route("/") (1: " " 사이에 도메인명 다음에 붙을 주소를 씁니다.)
def index():
    return render_template('index.html') (2: 주소에 해당되는 템플릿 이름을 씁니다.)


'''


@app.route("/")
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
