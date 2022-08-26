import os
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


database_name = "carbookdb"
database_path = "postgresql://{}:{}@localhost:5432/{}".format("postgres", "you password", database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    '''
      binds Flask application and SQLAlchemy service
      
      INPUT:
      app: instance of Flask application
      database_path: database uri, by default it takes the database_path from models
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
class Car(db.Model):
    '''Car Model'''
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    image_link = Column(String)
    
    def __init__(self, name, model, image_link):
        self.name = name
        self.model = model
        self.image_link = image_link
        
    def insert(self):
        '''Add new car'''
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        '''Update car by id'''
        db.session.commit()
        
    def delete(self):
        '''Delete car by id'''
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        '''Use to format data(car)'''
        return {
          "id": self.id,
          "name": self.name,
          "model": self.model,
          "image_link": self.image_link
        }

    