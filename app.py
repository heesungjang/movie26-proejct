from pymongo.encryption import Algorithm
import requests
from datetime import (datetime, timedelta)


from bs4 import BeautifulSoup
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


client = MongoClient('localhost', 27017)
db = client.mini_project

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    is_logedin = False

    if is_logedin is True:
        return render_template("index.html")
    else:
        return render_template("login.html")

@app.route("/auth/login", methods=["POST"])
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
                token = create_access_token(payload)
                return jsonify({'result': "success", "token": token})
            else:
                return jsonify({'result': "fail", "msg": "아이디, 비밀번호를 확인해주세요."})
            
@app.route("/auth/signup", methods=["POST"])
def signup():
    """
    회원가입 기능
    """
    if request.method == "POST":
        name_receive = request.form['name_give']
        username_receive = request.form['username_give']
        email_receive = request.form['email_give']
        password_receive = request.form['password_give']
        password2_receive = request.form['password2_give']

        if (password_receive == password2_receive):
            hashed_password = bcrypt.generate_password_hash(password_receive, 10).decode("utf-8")
            
            doc = {
            "name": name_receive,
            "username": username_receive,
            "email": email_receive,
            "password": hashed_password
            }
            
            db.users.insert_one(doc)
            return jsonify({'result': "success.", "msg": "회원가입 성공."})
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
            return jsonify({"movies": movie_dict, "msg": "success."})

@app.route("/movie/<movie_id>", methods=["GET"])
def movie_detail(movie_id):
    """
    영화 상세 페이지 정보 불러오기
    """
    movie = db.movie_details.find_one({'movie_id': int(movie_id)}, {"_id": False})
    if movie is not None:
        return jsonify({"movie": movie, "msg": "success."})


@app.route("/movie/<movie_id>/comment", methods=["POST"])
def comment(movie_id):
    """
    여기서 댓글 기능 구현
    """
    if request.method == "POST":
        user = db.users.find_one({"username": "heesungj7"}) ##dummy username data
        
        user_id = str(user["_id"])
        movie_id = 1 ## dummy data
        comment = "I like this movie!!" # dummy data
        
        doc ={
            "user_id": user_id,
            "movie_id": movie_id,
            "comment": comment,
        }
        db.comments.insert_one(doc)
        return jsonify({"asd":"asd"})
    

@app.route("/movie/1/like", methods=['POST'])
def like():
    token_receive = request.cookies.get('token')
    payload = jwt.decode(token_receive, SECRET_KEY, algoritims=['HS256'])
    user_info = db.users.find_one({"username": payload["id"]}
    
    movie_id_receive = request.form["movie_id_give"]
    action_receive = request.form["action_give"]

    doc = {
        "movie_id": movie_id_receive,
        "user_id": user_info["username"], 
    }

    if action_receive =="like":
        db.likes.insert_one(doc)
    else:
        db.likes.delete_one(doc)
    for post in like:
        post["heart_by_me"] = bool(db.likes.find_one({"movie_id": movie["_id"], "type": "heart", "username": payload"id}))
    return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "posts": posts})  
      
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

