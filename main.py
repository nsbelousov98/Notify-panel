
import os
from flask import Flask, render_template, request, redirect
from logic.handlers import handle_submission
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
requests_storage = []

@app.route('/')
def index():
    return render_template('index.html', requests=requests_storage)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    requests_storage.append(form_data)
    handle_submission(form_data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
