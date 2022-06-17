from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from pymongo import ASCENDING

from ..config import Settings
from ..db import Database


class Service:

	# variables
	config = Settings().settings()

	# connect to db
	db = Database().connect()

	# get data for dashboard
	async def get_dashboard(self):
		# data = (
		#     await self.db["genZ"].find({"sentence_entities" : {"$elemMatch": { "$elemMatch": {"$in": ['Stanford University']} } } }, projection={"_id": 1}).to_list(length=None)
		# )

		data = (
			await self.db["genZ"]
			.aggregate(
				[
					{"$match": {"sentence_entities": { "$not": {"$size": 0 } }}},
					{"$project": {"sentence_entities": 1}},
					{ "$unwind": "$sentence_entities"},
					{
						"$group": {
							"_id": "$sentence_entities",

							"size": {"$sum": 1}
						}
					},
					# { "$match": {"_id":  {"$elemMatch": {"$in": ['Stanford University']}}}},
					{"$sort": {"size": ASCENDING}},
				]
			)
			.to_list(100)
		)

		if data == None:
			raise HTTPException(
				status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="database went wrong"
			)

		return JSONResponse(status_code=status.HTTP_200_OK, content=data)
