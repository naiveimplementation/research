from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import jinja2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base, Temp

from Algorithm_NB import nb

engine = create_engine('sqlite:///temperatures.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


### Pages
@app.route('/', methods = ['POST', 'GET'])
def Home():
	if request.method == "POST":
		temp = int(request.form.get("temp", 0))
		fever = request.form.get("fever", False)
		if fever == "True":
			fever = True
		else:
			fever = False

		data_point = Temp(temp=temp, fever=fever)
		session.add(data_point)
		session.commit()
		return render_template('index.html')
	return render_template('index.html')

@app.route('/api')
def points():
	printing()
	temps = session.query(Temp).all()
	return jsonify(Temp=[t.serialize for t in temps])

def printing():
	print(nb())

if __name__== "__main__":
	app.run(debug=True)
