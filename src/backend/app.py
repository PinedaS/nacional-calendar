from scraper import run
from flask import Flask

app = Flask(__name__)


@app.get('/api/info-football-match')
def home():
    info = run()

    return info


if __name__ == '__main__':
    app.run(debug=True)
