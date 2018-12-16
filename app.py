from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Source : https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/
#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

e = create_engine('sqlite:///firstdb.db')

app = Flask(__name__)
api = Api(app)

class AskNumbers(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from firstdb")
        return {'1985': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(AskNumbers, '/data')

if __name__ == '__main__':
     app.run()
