import requests
import traceback
from typing import List
from requests import Response
from logging import Handler, LogRecord
from ...helpers.discordHelper.FormatterEmbed import FormatterEmbed

MAX_LOG_LENGTH = 2000

class WebhookHandler(Handler):
    def __init__(self, webhook_url: str):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record: LogRecord):
        try:
            
            log_message = self.format(record)
            content = "<@918684175178031124>" if record.levelname == "ERROR" else ""
            embeds = []
            
            if isinstance(record.msg, dict):
                embeds.append(record.msg)
            
            if isinstance(record.msg, str):
                messages: List[str] = split_message(log_message)
                
                for message in messages:
                    embed = FormatterEmbed().logger(record.levelname, message)
                    embeds.append(embed)
                
            res = requests.post(self.webhook_url, json={"content":content, "embeds":embeds})
                
            if res.status_code != 204:
                self._fail_request(res)   
                            
        except Exception:
            print(traceback.format_exc())
            
    def _fail_request(self, res: Response):
        print(f"source/config/logger/WebhookHandler.py:WebhookHandler()._fail_request\n-> {res.status_code} - {res.text}")
            
def split_message(message: str) -> list:
    
    if len(message) <= MAX_LOG_LENGTH:
        return [message]
    
    return [message[i:i+MAX_LOG_LENGTH] for i in range(0, len(message), MAX_LOG_LENGTH)]