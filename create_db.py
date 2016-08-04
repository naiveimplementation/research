from sqlalchemy import Column, Integer, Boolean, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///temperatures.db')
Base.metadata.bind = engine

class Temp(Base):
	__tablename__ = 'temp'
	id = Column(Integer, primary_key=True)
	temp = Column(Float)
	fever = Column(Boolean)

	@property
	def serialize(self):
		return {
			'temp': self.temp,
			'fever': self.fever
		}

Base.metadata.create_all(engine)