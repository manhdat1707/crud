from flask_redis import Redis
from flask import Flask,jsonify,request,Response
from peewee import *
import json



# connect database
#
db = MySQLDatabase('dbname', user='root', passwd='my-secret-pw',host='127.0.0.1', port=3307)
class Movies (Model):
    title = TextField()
    genre = TextField()
    year = CharField()
    class Meta:
      database=db
      db_table='Movies'
    def json(self):
        return {'id': self.id, 'title': self.title,'year': self.year, 'genre': self.genre}
    def get_movies():
       # return list(Movies.select()) 
        return [Movies.json(movie) for movie in Movies.select()]
    def save_movie(title, year, genre):
        Movies.create( title=title,year = year, genre=genre)
    def get_movie_by_id(_id):
        return [Movies.json(Movies.get_by_id(_id))]
    def delete_movie(id):
            Movies.delete_by_id(id)
    def update_movie(id,title, year, genre):
        Movies.update( title=title, year = year, genre = genre).where(Movies.id)
    
db.connect()
db.create_tables([Movies])





        
app = Flask(__name__)
app.config['REDIS_HOST'] = '127.0.0.1'
app.config['REDIS_PORT'] = 6379
redis_cache = Redis(app)

@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()
