from flask import Flask, abort, render_template, request, redirect
from db import get_shortened, add_shortened
from utils import get_available_key, is_valid_url

app = Flask(__name__)

baseURL = app.config.get('BASE_URL') or "http://localhost:5000/"

# Home page
@app.route("/", methods=["GET"])
def home():
  return render_template('index.html')

# Lookup shortened URL and redirect
@app.route("/<key>", methods=["GET"])
def lookup_url(key):
  shortened = get_shortened(key)

  if (shortened == None):
    abort(404)

  return redirect(shortened[1])

# API shortening endpoint
@app.route("/api/shorten", methods=["POST"])
def shorten():
  url = request.json.get('url')

  if (url == None or is_valid_url(url) == False):
    abort(400)

  key = get_available_key()
  add_shortened(key, url)

  return { "url": baseURL + key }
