from .services import Service
from ..utils.auth import Auth

class Handler:
    
	auth = Auth()
	service = Service()

	async def get_dashboard(self, request):
		return await self.auth.protector(request, self.service.get_dashboard)
