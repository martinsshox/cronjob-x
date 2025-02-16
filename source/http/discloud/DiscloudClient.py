import aiohttp
import requests
from ...config.Env import Env

class DiscloudClient:
    def __init__(self, token: str):
        
        self._token = token
        self._base_url = Env.DISCLOUD_BASE_URL
        self._headers = {"api-token": self._token}

    async def _make_request(self, method: str, route: str) -> dict:

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                self._base_url+route,
                headers=self._headers
                ) as response:

                if response.status != 200:
                    raise Exception(f"-> {response.status} - {await response.text()}")
                
                return await response.json()

    async def _make_request_put(self, route: str) -> dict:
        response = requests.put(self._base_url+route, headers=self._headers)
        
        if response.status_code != 200:
                raise Exception(f"-> {response.status_code} - {response.text}")
            
        return response.json()

    async def get_logs_app(self, app_id: str) -> dict:

        response = await self._make_request(
            "GET",
            f"{app_id}/logs"
        )
        
        return response

    async def restart_app(self, app_id: str) -> None:

        await self._make_request_put(
            f"{app_id}/restart"
        )
