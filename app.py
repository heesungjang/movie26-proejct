from flask.helpers import url_for
import flask_jwt_extended
from pymongo.encryption import Algorithm
import requests
from datetime import (datetime, timedelta)
import jwt

from bs4 import BeautifulSoup
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, redirect




client = MongoClient('localhost', 27017)
db = client.mini_project

app = Flask(__name__)
SECRET_KEY= "SPARTA"
bcrypt = Bcrypt(app)

@app.route("/", methods=["POST", "GET"])
def index():
 
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"username": payload['id']})
        doc = {
            "username": payload['id']
        }
        return render_template("index.html", username=doc)
    except jwt.ExpiredSignatureError:
        return redirect("/auth/login")
    except jwt.exceptions.DecodeError:
        return redirect("/auth/login")

@app.route("/auth/login", methods=["POST", "GET"])
def login():
    """
    로그인 기능
    """
    if request.method == "POST":
        
        username_receive = request.form['username_give']
        password_receive = request.form['password_give']

        username_result = hashed_password = db.users.find_one({'username': username_receive}, {"_id": False})["username"]

        if username_result is not None:
            hashed_password = db.users.find_one({'username': username_receive}, {"_id": False})["password"]
            
            password_result = bcrypt.check_password_hash(hashed_password, password_receive) 

            if password_result is True:
                payload ={
                    'id': username_receive,
                    'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                return jsonify({'result': "success", "token": token})
            else:
                return jsonify({'result': "fail", "msg": "아이디, 비밀번호를 확인해주세요."})
    elif request.method == "GET":
        return render_template("login.html")
        
@app.route("/auth/signup", methods=["POST", "GET"])
def signup():
    """
    회원가입 기능
    """
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username_receive = request.form['username_give']
        email_receive = request.form['email_give']
        password_receive = request.form['password_give']
        password2_receive = request.form['password2_give']

        if (password_receive == password2_receive):
            hashed_password = bcrypt.generate_password_hash(password_receive, 10).decode("utf-8")
            
            doc = {
            "username": username_receive,
            "email": email_receive,
            "password": hashed_password
            }
            
            db.users.insert_one(doc)
            return jsonify({'result': "success", "msg": "회원가입 성공."})
    else:
        return jsonify({'result': "fail", "msg": "비밀번호가 일치하지 않습니다."})

@app.route("/movie/list", methods=["GET"])
def get_movies():
    """
    영화 리스트 불러오기
    """
    if request.method == "GET":
        movie_dict = list(db.movie_details.find({}, {"_id": False})[0:])
        if movie_dict is not None:
            return jsonify({"movies": movie_dict, "msg": "success"})

@app.route("/movie/<movie_id>", methods=["GET"])
def movie_detail(movie_id):
    """
    영화 상세 페이지 정보 불러오기
    """
    token_receive = request.cookies.get("mytoken")
    if token_receive is None:
        return redirect("/")


    movie = db.movie_details.find_one({'movie_id': int(movie_id)}, {"_id": False})
    reviews = db.comments.find({'movie_id': movie_id})
    

    if movie is not None:
        return render_template("detail.html", movie=movie, reviews=reviews)


@app.route("/movie/<movie_id>/comment", methods=["POST"])
def comment(movie_id):
    """
    여기서 댓글 기능 구현
    """
    if request.method == "POST":
        token_receive = request.cookies.get("mytoken")
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])


        username = (payload["id"])
        movie_id_receive = movie_id 
        comment_receive= request.form["comment_give"]
        
        doc ={
            "user_id": username,
            "movie_id": movie_id_receive,
            "comment": comment_receive,
        }
        db.comments.insert_one(doc)
        return jsonify({"result": "success", "msg": "댓글를 추가했습니다."})

@app.route("/movie/<movie_id>/comment/delete", methods=["POST"])
def del_comment(movie_id):
    if request.method == "POST":

        token_receive = request.cookies.get("mytoken")
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        username = (payload["id"])

        comment_receive = request.form["comment_give"]
        target_comment = db.comments.find_one({"user_id": username, "movie_id": movie_id, "comment": comment_receive})
        
      
        if target_comment is not None:
            db.comments.delete_one({"user_id": username, "movie_id": movie_id, "comment": comment_receive})
            
            return jsonify({"result": "success", "msg": "댓글 삭제"})
        else:
            return jsonify({"result": "fail", "msg": "다른 사람의 댓글은 삭제할 수 없습니다."})

@app.route("/movie/1/like")
def like():
    token_receive = request.cookies.get("mytoken")
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    username = db.users.find_one({"username": payload["id"]})
    
    # movie_id_receive = movie_id
    # action_receive = request.form["action_give"]
    action_receive ="like"
    doc ={
    "user_id": "heesungj7", 
    "movie_id": 1,
    "action": "like"
    }

    if action_receive =="like":
        db.likes.insert_one(doc)
        count = db.likes.count_documents({"movie_id": 1, "action": "like"})
        print(count)
        return render_template("login.html")
    else:
        db.likes.delete_one(doc)
    # for post in like:
    #     post["heart_by_me"] = bool(db.likes.find_one({"movie_id": movie["_id"], "type": "heart", "username": payload"id}))
    return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다."})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)








