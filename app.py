#-*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


'''
주소 추가방법을 설명합니다!

@app.route("/") (1: " " 사이에 도메인명 다음에 붙을 주소를 씁니다.)
def index(): (2: 함수의 이름을 정합니다. (주소와 비슷하게 합니다. _ 와 숫자, 영문자만 쓸 수 있습니다.))
    return render_template('index.html') (3: 주소에 해당되는 템플릿 이름을 씁니다.)


'''


@app.route("/")
def index():
    return render_template('index.html')


# 카테고리 페이지들
@app.route("/category/1")
def category_1():
    return render_template('portfolio-category-1.html')


@app.route("/category/2")
def category_2():
    return render_template('portfolio-category-2.html')


@app.route("/category/3")
def category_3():
    return render_template('portfolio-category-3.html')


@app.route("/category/4")
def category_4():
    return render_template('portfolio-category-4.html')


@app.route("/portfolio/1")
def portfolio_1():
    return render_template('portfolio-item-1.html')


@app.route("/portfolio/2")
def portfolio_2():
    return render_template('portfolio-item-2.html')


@app.route("/portfolio/3")
def portfolio_3():
    return render_template('portfolio-item-3.html')


@app.route("/portfolio/4")
def portfolio_4():
    return render_template('portfolio-item-4.html')


@app.route("/portfolio/5")
def portfolio_5():
    return render_template('portfolio-item-5.html')


@app.route("/portfolio/6")
def portfolio_6():
    return render_template('portfolio-item-6.html')


@app.route("/portfolio/7")
def portfolio_7():
    return render_template('portfolio-item-7.html')


@app.route("/portfolio/8")
def portfolio_8():
    return render_template('portfolio-item-8.html')


if __name__ == "__main__":
    app.run(debug=True)
