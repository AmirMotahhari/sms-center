from abc import ABCMeta, abstractmethod


class StorageBase(metaclass=ABCMeta):
    _host = None
    _port = None
    _username = None
    _password = None

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def get(self, row_id):
        pass

    @abstractmethod
    async def write(self, **kwargs):
        pass

    @abstractmethod
    async def delete(self, row_id):
        pass

    @abstractmethod
    async def disconnect(self):
        pass
