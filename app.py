from flask import Flask, render_template, request, jsonify
from modules.query_handler import handle_query

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    user_lang = request.json['language']
    response = handle_query(user_input, user_lang)
    return jsonify({'response': response})
if __name__ == "__main__":
    app.run(debug=True)