from flask_restful import Resource

from app.controllers.rope import RopeController


class RopeCollection(Resource):

    def get(self):
        ropes = RopeController().fetch_many()
        return {'data': ropes}, 200
