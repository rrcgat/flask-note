import json

from flask import Flask, request

from database import db_session, engine
from models import NoteInfo, Notebooks

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is mini note app'

@app.route('/u', methods=['POST'])
def upload():
    if request.method == 'POST':
        _content = json.loads(request.values.get('content'))
        _type = request.values.get('type')
        ts = str(_content['ts'])
        print(_content)
        print(_type)
        if _type == 'book':
            if _content['update']:
                data = Notebooks.query.filter_by(ts=ts).first()
                data.bookname = _content['name']
            else:
                data = Notebooks(ts, _content['name'])
        elif _type == 'note':
            if _content['update']:
                data = NoteInfo.query.filter_by(ts=ts).first()
                data.note = _content['note']
            else:
                data = NoteInfo(ts, _content['bookid'],
                                _content['note'])
        db_session.add(data)
        db_session.commit()
        return '200'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='192.168.1.122', port=5000)
