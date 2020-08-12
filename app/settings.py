from dataclasses import dataclass
from os import environ


def get_settings() -> dict:
    return {
        'rei': {
            'base_url': environ.get('REI_BASE_URL', 'placeholder'),
            'rope_path': environ.get('REI_ROPE_PATH', 'placeholder')
        }
    }
