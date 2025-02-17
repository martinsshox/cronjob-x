import traceback
from collections import deque
from datetime import datetime
from source.config.logger.logger import logger
from source.clients.discloud.DiscloudClient import DiscloudClient
from source.helpers.discordHelper.FormatterEmbed import FormatterEmbed

class DiscloudCronJob():
    def __init__(self, client: DiscloudClient, app_id: str):
        self._client = client
        self._embed = FormatterEmbed()
        self._app_id = app_id
        self._online = False
        self._latest_logs: deque[str] = None
        self._positive_log: str = None
        self._initialized_at = datetime.now()
        self._checked_at: datetime = None
        self._restarted_at: datetime = None
        
    async def initialize(self):
        
        try:
        
            latest_logs = self._latest_logs
            await self._check_status()
            recents_logs = self._latest_logs
            
            if not self._online:
                
                embed = self._embed.application_off(self._latest_logs, self._checked_at)
                logger.error(embed)
                
                await self._restart()
                await self._check_status()
                
                embed = self._embed.application_startup(self._latest_logs, self._checked_at, self._restarted_at)
                logger.error(embed)
                
                return
            
            if latest_logs == recents_logs:
                logger.warning(f"A verificação foi poupada, não há novas requisições!\n\n**LOG ANTERIOR:**\n```{latest_logs[8]}```\n\n**LOG RECENTE:**\n```{recents_logs[8]}```")
                return
            
            embed = self._embed.application_on(self._latest_logs, self._positive_log, self._checked_at, self._restarted_at, self._initialized_at)
            logger.debug(embed)
            
        except Exception:
            print(traceback.format_exc())
        
    async def _check_status(self):
        
        response = await self._client.get_logs_app(self._app_id)
        logs: str = response["apps"]["terminal"]["big"]
        
        logs = logs.split("\n")
        recent_logs = deque(logs[-10:], maxlen=10)

        self._checked_at = datetime.now()
        
        if self._latest_logs == recent_logs:
            return

        self._online = False
        self._latest_logs = recent_logs
        
        for log in reversed(recent_logs):    
            if "INFO:" in log:
                self._online = True
                self._positive_log = log
                break
            
    async def _restart(self):
        await self._client.restart_app(self._app_id)
        self._restarted_at = datetime.now()