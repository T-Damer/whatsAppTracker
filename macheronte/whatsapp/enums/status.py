from enum import Enum

class Status(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    IS_WRITING = 'is writing...'
    NOT_DEFINED = 'not defined'