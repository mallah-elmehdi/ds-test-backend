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
		youngPeopledataSample = (
		    await self.db["young_people"].find({}, projection={"logits": 1}).to_list(length=None)
		)

		genZdataSample = (
			await self.db["genZ"]
			.aggregate(
				[
					{
						"$group": {
							"_id": "$category",
							"sentence_sent_score": {"$sum": "$_id"}
						}
					},
					{"$sort": {"sentence_sent_score": ASCENDING}},
				]
			)
			.to_list(length=None)
		)

		if youngPeopledataSample == None or genZdataSample  == None:
			raise HTTPException(
				status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="database went wrong"
			)

		return JSONResponse(status_code=status.HTTP_200_OK, content={"genZ": genZdataSample, "youngPeople": youngPeopledataSample})
