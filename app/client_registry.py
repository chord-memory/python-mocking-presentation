from app.clients.rei import ReiClient


class ClientRegistry:

    def __init__(self, settings):
        self.rei_settings = settings['rei']


    def get_clients_with_rope(self):
        return [
            ReiClient(**self.rei_settings)
        ]
