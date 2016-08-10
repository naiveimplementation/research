from sqlalchemy import Column, Integer, Boolean, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

class Datapoint(Base):
	__tablename__ = 'data'
	id = Column(Integer, primary_key=True)
	grade = Column(Integer)
	bump = Column(Integer)
	speed = Column(Boolean)

	@property
	def serialize(self):
		return {
			'grade': self.grade,
			'bump': self.bump,
			'speed': self.speed
		}

Base.metadata.create_all(engine)