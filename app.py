from flask import Flask, render_template, request, jsonify
from models import db, ScrapedData
from scrape import scrape_website
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    url = request.values.get('url')
    if not url:
        return jsonify({'error': 'no url provided'}), 400

    result = scrape_website(url)
    if not result:
        return jsonify({'error': 'scrape failed'}), 500

    try:
        sd = ScrapedData(
            url=result['url'],
            content=result['content'],
            word_frequency=result['word_frequency'],
            created_at=datetime.utcnow()
        )
        db.session.add(sd)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'db error', 'details': str(e)}), 500

    return jsonify({'status': 'ok', 'id': sd.id}), 201


@app.route('/data')
def data():
    url = request.args.get('url')
    sid = request.args.get('id', type=int)
    top_n = request.args.get('limit', default=20, type=int)

    if sid:
        sd = ScrapedData.query.get(sid)
    elif url:
        sd = ScrapedData.query.filter_by(url=url).order_by(ScrapedData.created_at.desc()).first()
    else:
        sd = ScrapedData.query.order_by(ScrapedData.created_at.desc()).first()

    if not sd:
        return jsonify({'labels': [], 'values': []})
    wf = sd.word_frequency or {}
    # Some backends may store the JSON as a string; coerce to dict
    if isinstance(wf, str):
        try:
            wf = json.loads(wf)
        except Exception:
            wf = {}
    if not isinstance(wf, dict):
        try:
            wf = dict(wf)
        except Exception:
            wf = {}

    # Helpful debug output (appears in server console)
    try:
        print(f"/data -> source_id={sd.id} url={sd.url} tokens={len(wf)}")
    except Exception:
        pass
    items = sorted(wf.items(), key=lambda x: x[1], reverse=True)[:top_n]
    labels = [i[0] for i in items]
    values = [i[1] for i in items]
    return jsonify({'labels': labels, 'values': values, 'source_id': sd.id, 'url': sd.url})


if __name__ == '__main__':
    app.run(debug=True)
