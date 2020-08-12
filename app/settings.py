from dataclasses import dataclass
from os import getenv


def get_settings() -> dict:
    return {
        'rei': {
            'base_url': getenv('REI_BASE_URL'),
            'rope_path': getenv('REI_ROPE_PATH')
        }
    }
