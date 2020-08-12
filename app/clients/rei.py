import requests
from os import path
from typing import List

from app.clients.interface import HasRope
from app.models.rope import RopeModel


class ReiClient(HasRope):

    def __init__(self, base_url, rope_path):
        self._rope_endpoint = path.join(base_url, rope_path)

    def fetch_ropes(self) -> List[RopeModel]:
        ropes = requests.get(self._rope_endpoint)
        rope_models = []
        for rope in ropes:
            rope_models.append(
                RopeModel(
                    rope.get('diameter'),
                    rope.get('length'),
                    rope.get('brand'),
                    rope.get('color'),
                    rope.get('price')
                )
            )
        return rope_models
