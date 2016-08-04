from flask import Flask, render_template, jsonify
app = Flask(__name__)
import jinja2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base, Temp

engine = create_engine('sqlite:///temperatures.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


### Pages
@app.route('/')
def Show():
	return render_template('index.html')

@app.route('/api')
def mammals():
	temps = session.query(Temp).all()
	return jsonify(Temp=[t.serialize for t in temps])

if __name__== "__main__":
	app.run(debug=True)
