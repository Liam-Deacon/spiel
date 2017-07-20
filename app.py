from flask import Flask,render_template
spiel_app = Flask(__name__)

@spiel_app.route('/')
def index_lulu():
    return render_template('index.html')

if __name__ == "__main__":
    spiel_app.run(debug=True, port=5003)
