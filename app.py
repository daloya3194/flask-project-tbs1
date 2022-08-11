from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lwodyxevucbixp:1a43be9374c689ae655a1193640e10b37a9da07ba7880891d16572113ea6e94c@ec2-100-26-39-41.compute-1.amazonaws.com:5432/d2bnrqkqle25s9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
