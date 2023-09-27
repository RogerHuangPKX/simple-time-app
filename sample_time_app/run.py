from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def returnTime():
    from datetime import datetime
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now+"\n Jinze Huang \n NetID:jh9108\n"


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
