import json

from flask import Flask, request, render_template

from database import db_session, engine
from models import NoteInfo, Notebooks

app = Flask(__name__)


@app.route('/')
def index():
    notebooks = NoteInfo.query.all()[:10]
    return render_template('index.html', notebooks=notebooks)

@app.route('/d', methods=['POST'])
def delete():
    ts = request.values.get('ts')
    _type = request.values.get('type')
    if _type =='book':
        data = Notebooks.query.filter_by(ts=ts).first()
    else:
        data = NoteInfo.query.filter_by(ts=ts).first()
    db_session.delete(data)
    db_session.commit()
    return '1'

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
