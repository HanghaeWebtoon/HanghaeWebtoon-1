from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# pyMongo
# URL 이스케이프 문자 : https://namu.wiki/w/URL%20escape%20code
client = MongoClient(
    'mongodb+srv://swlah:%40zbqm1075711@cluster0.g93fmw7.mongodb.net/?retryWrites=true&w=majority')
db = client.webtoon

# index.html
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

# 회원가입 페이지
@app.route("/register", methods=["POST"])
def register_post():
    user_receive = request.form['user_give']
    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']
    pw_check_receive = request.form['pw_check_give']

    if pw_receive != pw_check_receive:
        return jsonify({'msg': '비밀번호가 일치하지 않습니다.'})

    doc = {
        'username': user_receive,
        'mail': email_receive,
        'password': pw_receive
    }

    db.user.insert_one(doc)

    return jsonify({'msg':'회원가입 완료!'})

@app.route("/register", methods=["GET"])
def register_get():
    return render_template('register.html')

# 로그인 페이지
@app.route("/login", methods=["POST"])
def login_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'login Page POST 연결 완료!'})

@app.route("/login", methods=["GET"])
def login_get():
    return render_template('login.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
