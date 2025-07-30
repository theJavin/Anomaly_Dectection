from flask import Flask, render_template, request, Response, jsonify, send_file
from datetime import datetime
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/track-mouse', methods=['POST'])
def track_mouse():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    index = data.get('index')
    date = datetime.now()
    with open('mouse_log.txt', 'a') as f:
        f.write(f"{date}, {index}, {x}, {y}\n")
    return jsonify({"status": "success"})



if __name__ == '__main__':
    app.run(debug=True)