from datetime import datetime
import os,time,json
from flask import Flask, request,jsonify
from flask import render_template
from flask_cors import CORS
import readvec 
from qsresouce import *
import pickle
queList=[]
ansList=[]
readQSresouce('wordresource.txt',queList,ansList)

with open('embedding.pickle', 'rb') as handle:
    vectors = pickle.load(handle)
# 用vectors从embedding.pickle中读取全部词向量

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/check",methods=['post'])
def check():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('qsSystem.html')
    return render_template("login.html",answer="wrong")


@app.route("/question",methods=['post'])
def add():
    ques=request.form['question'].replace('\n','')#去除回车
    ans=request.form['answer'].replace('\n','')
    queList.append(ques)
    ansList.append(ans)
    file1=open("wordresource.txt","a")
    file1.write('\n')
    file1.write(ques)
    file1.write('\n')
    file1.write(ans)
    file1.close()
    return render_template('qsSystem.html',answer="success")
    

@app.route("/hello")
def hello():
    return "hello"


@app.route("/chatbot")
def chat():
    tmpcontent = request.args.get('content')
    content=tmpcontent.replace('\n','')
    answer=readvec.similarityCheck(content,vectors,queList,ansList)
    print(content)
    print(answer)
    return  json.dumps({'as':answer}) 


if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
    #debug=True,debug模式会产生双倍的内存消耗



# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 80))
#     app.run(host='0.0.0.0', port=port, debug=True)#coding:utf8

