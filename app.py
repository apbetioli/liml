from flask import Flask, request
import json
from meli import Meli
import os

meli = Meli(client_id=os.environ['CLIENT_ID'],client_secret=os.environ['CLIENT_SECRET'])

app = Flask(__name__)

@app.route('/')
def login():
    href = meli.auth_url(redirect_URI=request.url_root+'authorize')
    return '<a href="'+href+'">Login</a>'

@app.route('/authorize')
def authorize():
    if request.args.get('code'):
        meli.authorize(request.args.get('code'), request.url_root+'authorize')
    print(meli.access_token)
    return meli.access_token

