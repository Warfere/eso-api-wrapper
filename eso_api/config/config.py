from .creds import api_key


class Config:
    def __init__(self):
        self.settings = {"api_key": api_key}

    def update(self, config_dict):
        self.settings.update(config_dict)
