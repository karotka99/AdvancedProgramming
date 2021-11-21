from flask import Flask
from flask_restful import Resource, Api
import services.utils
import Models.Movie

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        file = services.utils.readfile(r'C:\Users\Karolina\PycharmProjects\lab_7\data\movies.csv')
        splitfile = file.split('\n')
        splitfile.pop(0)
        splitfile.pop(len(splitfile)-1)
        ListOfFilms = []
        for movies in splitfile:
            movie = movies.split(',')
            ListOfFilms.append(Models.Movie.Movie(movie[0], movie[1], movie[2]).__dict__)
        return ListOfFilms


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
