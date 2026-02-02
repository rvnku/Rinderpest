import os
from abc import ABC
from typing import Final
from dotenv import load_dotenv


load_dotenv('./.env')


class Config(ABC):
    CMD_PREFIX: Final = '.'
    ID_GUILD: Final = int(os.environ.get('ID_GUILD', 0))
    STANDARD_EXTENSIONS: Final = ['owner.loader', 'owner.command', 'owner.presence']
