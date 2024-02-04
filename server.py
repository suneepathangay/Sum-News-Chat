
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from algo import return_summary
import os
from chatbot.chat import send_text_bot,chat_with_bot
import subprocess
import os

##server for flask app
#deploy the app

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})
os.environ["REPLICATE_API_TOKEN"] = "r8_3xeN30VMmlVslWSSjuQxwgwZXhfRpDA3xUIQU"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dash')
def get_dash():
    return render_template('dash.html')

@app.route('/summ')
def get_summ():
    return render_template('summ.html')


@app.route('/ocr')
def get_ocr():
    return render_template('ocr.html')

@app.route('/results',methods=["POST"])
def process_text():
    data=request.get_json()
    article=data['text']
    summary=return_summary(article)
    
    response = jsonify({"summary": summary})
    response.headers.add("Access-Control-Allow-Origin", "http://192.168.68.62:5000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    
    return response

@app.route('/chat',methods=["GET"])
def chat():
    return render_template('chat.html')


@app.route('/chat-text',methods=["POST"])
def send_text():
    
    result=None
    text=request.get_json()
    text=text['text']
    if len(text.split(" ")) >= 50:
        send_text_bot(text)
        result="Text successfully uploaded"
    else:
        result=chat_with_bot(text)
        
    print(result)
    response=jsonify({"result":result})
    response.headers.add("Access-Control-Allow-Origin", "http://192.168.68.62:5000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    
    return response

if( __name__ =='__main__'):
    app.run(host="0.0.0.0",port=5000,debug=True)