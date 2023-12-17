from flask import Flask, redirect, abort
from get_stream import get_stream

app = Flask(__name__)

@app.route("/")
def main():
  stream = get_stream()
  
  if stream is not None:
    return redirect(stream, code=302)
  
  abort(404)
