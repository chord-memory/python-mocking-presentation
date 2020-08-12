from flask_restful import Resource

from app import settings
from app.clients.rei import ReiClient
from app.controllers.rope import RopeController


class RopeCollection(Resource):

    _clients_with_rope = [
        ReiClient(**settings['rei'])
    ]

    def get(self):
        ropes = RopeController().fetch_many(
            self._clients_with_rope
        )
        return {'data': ropes}, 200
