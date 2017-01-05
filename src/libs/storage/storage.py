# FIXME: need more consideration on import drivers & connect to db (singletone)
import os


class Storage:
    """This is the main class of storage which
       has access to the databases drivers.
    """
    def __init__(self, driver_name, config):
        self.config = config
        self.driver_name = driver_name
        self.driver = None
        self.database = None

    async def import_driver(self):
        if os.path.exists(os.path.join('./drivers/', "{}.py".format(self.driver_name))):
            self.driver = __import__('drivers.{}'.format(self.driver_name), fromlist=self.driver_name.capitalize())
            self.database = getattr(self.driver_name, self.driver_name.capitalize())
        else:
            raise RuntimeError('Database driver not found!')

    async def connect(self):
        """
        Connect to the database with driver.

        :return: True/Raise Exception
        """
        self.database.connect()

    async def prepare_connection(self):
        """Prepare connection for database."""
        await self.import_driver()
        await self.connect()

    async def new(self, data):
        """
        Insert new data in database.

        :param data: dictionary of data (key: field, value: data).
        :return: True/False
        """
        await self.prepare_connection()
