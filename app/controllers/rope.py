from typing import List
from dataclasses import asdict

from app import client_registry
from app.models.rope import RopeModel


class RopeController:

    def fetch_many(self) -> List[dict]:
        clients_with_rope = client_registry.get_clients_with_rope()
        rope_models = []
        for client in clients_with_rope:
            rope_models += client.fetch_ropes()
        return [asdict(rope_model) for rope_model in rope_models]
