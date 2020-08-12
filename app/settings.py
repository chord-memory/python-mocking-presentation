import os
from dataclasses import dataclass


def get_settings() -> dict:
    return {
        'rei': {
            'base_url': os.environ.get('REI_BASE_URL', 'placeholder'),
            'rope_path': os.environ.get('REI_ROPE_PATH', 'placeholder')
        }
    }
