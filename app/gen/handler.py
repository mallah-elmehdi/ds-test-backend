from ..utils.auth import Auth


class Handler:

    auth = Auth()

    async def signin(self, request, user):
        return self.auth.is_signed(request, user, self.auth.signin)

    def get_signin(self, request):
        return self.auth.get_signed(request)
