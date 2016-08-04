from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base, Temp
import random

engine = create_engine('sqlite:///temperatures.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def addTemp():
	t = Temp(temp = 97, fever=True)
	session.add(t)
	session.commit()

for x in range(1):
	addTemp()
	
print("done.")