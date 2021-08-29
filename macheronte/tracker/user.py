from macheronte.whatsapp.client import WhatsappClient
from macheronte.whatsapp.enums.status import Status

from datetime import datetime


class User(object):
    def __init__(self, target: str, client: WhatsappClient):
        self.__target = target
        self.__client = client
        self.__status = None
        self.__has_new_status = False
        self.__header = None
        self.__new_user = True
        self.__db = []
        self.__notifications = False

    def sample(self):
        if self.__client.is_logged() and self.__client.open_chat(self.__target):
            self.__update_status(self.__client.get_user_status(self.__target))

    def has_new_status(self) -> bool:
        current_status = self.__has_new_status
        self.__has_new_status = False
        return current_status

    @property
    def status(self) -> Status:
        return self.__status

    @property
    def user_name(self) -> str:
        return self.__target

    @property
    def header(self):
        return self.__client.get_header()

    def is_new(self) -> bool:
        is_new = self.__new_user
        self.__new_user = False
        return is_new

    def is_valid(self) -> bool:
        return self.__client.open_chat(self.__target)

    @property
    def db(self):
        return self.__db

    @property
    def notifications_active(self) -> bool:
        return self.__notifications

    def set_notifications(self, active: bool):
        self.__notifications = active

    def __update_status(self, status: Status):
        if self.__status != status:
            self.__status = status
            self.__db.append((status, datetime.now()))
            self.__has_new_status = True
