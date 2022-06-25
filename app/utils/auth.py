from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from jose import jwt

from ..config import Settings


class Auth:

	# variables
	config = Settings().settings()

	# authenticatiion protector
	async def protector(self, request, call_next):
		# get the cookie
		cookie = request.cookies.get(self.config.cookie_name)

		# check the availability of the cookie
		if cookie == None:
			raise HTTPException(
				status_code=status.HTTP_401_UNAUTHORIZED, detail="user not logged in"
			)

		# check the user's cookie
		token = jwt.decode(cookie, self.config.jwt_secret, algorithms=[self.config.jwt_algorithm])

		if token["user_id"] != self.config.user_id:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user not allowed")

		return await call_next()

	# check if the user is already signed in
	def is_signed(self, request, user, call_next):

		# get the cookie
		cookie = request.cookies.get(self.config.cookie_name)

		# check the availability of the cookie
		if cookie != None:
			return JSONResponse(
				status_code=status.HTTP_401_UNAUTHORIZED, content="user already signed in"
			)

		return call_next(user)

	# signin
	def signin(self, user):
		if user.user_name != self.config.user_name or user.password != self.config.password:
			raise HTTPException(
				status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong credentials"
			)
		token = jwt.encode(
			{"user_id": self.config.user_id},
			self.config.jwt_secret,
			algorithm=self.config.jwt_algorithm,
		)
		# response = JSONResponse(status_code=status.HTTP_202_ACCEPTED, content="user signed in successfuly")
		response.set_cookie(key=self.config.cookie_name, value=token,  httponly=True, secure=True, samesite='none')
		return response

	# get_signin
	def get_signed(self, request):
		# get the cookie
		cookie = request.cookies.get(self.config.cookie_name)

		# check the availability of the cookie
		if cookie != None:
			return JSONResponse(
				status_code=status.HTTP_401_UNAUTHORIZED, content="user already signed in"
			)
		return JSONResponse(
			status_code=status.HTTP_200_OK, content="user is not signed in"
		)
