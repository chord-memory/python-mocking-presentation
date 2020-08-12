from app.client_registry import ClientRegistry
from app.settings import get_settings

settings = get_settings()
client_registry = ClientRegistry(settings)
