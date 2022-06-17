import motor.motor_asyncio
from .config import Settings

class Database:
	settings = Settings().settings()

	def connect(self):
		client = motor.motor_asyncio.AsyncIOMotorClient(str(self.settings.db))
		return client[str(self.settings.db_name)]
