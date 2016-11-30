"""Redis storage service driver."""
from .storage_base import StorageBase
import redis


class Redis(StorageBase):
    """Redis connection driver."""
    _connection = None
    _host = None
    _port = None
    _password = None

    def __init__(self, **config):
        self._host = config.get('host')
        self._port = config.get('port')
        self._password = config.get('password')

    def __new__(cls, *args, **kwargs):
        """Singletone implementation."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Redis, cls).__new__(cls)
        return cls.instance

    async def connect(self):
        """Connect to Redis storage."""
        if not self._connection:
            self._connection = redis.StrictRedis(self._host, self._port, self._password)
        return self._connection

    async def get(self, key):
        """Get value of key from redis."""
        await self.connect()
        return self._connection.get(key)

    async def write(self, key, value):
        await self.connect()
        try:
            self._connection.set(key, value)
            return True
        except:  # FIXME: need to handle exceptions.
            return False

    async def delete(self, keys):
        """Delete keys from redis."""
        await self.connect()
        keys = keys if isinstance(keys, list) else [keys]
        try:
            self._connection.delete(keys)
            return True
        except:  # FIXME: need to handle exceptions.
            return False

    async def disconnect(self):
        """No disconnect method."""
        pass
