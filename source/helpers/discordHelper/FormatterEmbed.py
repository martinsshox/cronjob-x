import discord
from collections import deque
from datetime import datetime

defaultEmbedsInfo = {
    "DEBUG": {
        "title": "MENSAGEM DE DEPURAÇÃO!",
        "thumbnail":"https://i.postimg.cc/HLTcTbYr/virus-scan.png",
        "color": 5324709
    },
    "WARNING": {
        "title": "MENSAGEM DE ALERTA!",
        "thumbnail":"https://i.postimg.cc/dV2ZM5YM/warning.png",
        "color": 15844367
    },
    "ERROR": {
        "title": "MENSAGEM DE ERRO!",
        "thumbnail":"https://i.postimg.cc/2SbT4RhQ/error.png",
        "color": 16711680  
    }
}

class FormatterEmbed:
    
    def __init__(self):
        self._EmbedAuthor = discord.EmbedAuthor("Discloud Monitor | APP Discord Shox", icon_url="https://i.imgur.com/Ipdl9AH.png")
        self._EmbedFooter = discord.EmbedFooter("Mensagem de registro enviada", "https://i.imgur.com/4ywUA3d.png")
        
    def application_startup(self, logs: deque[str], checked_at: datetime, restarted_at: datetime) -> dict:
    
        description = (
            "A aplicação API Discord Shox foi reiniciada com sucesso!\n\n"
            f"- ⏱️ | **Verificada <t:{int(checked_at.timestamp())}:R>**: <t:{int(checked_at.timestamp())}:f>.\n"
            f"- ♻️ | **Reiniciada <t:{int(restarted_at.timestamp())}:R>**: <t:{int(restarted_at.timestamp())}:f>.\n"
            f"{self._add_logs(logs)}"
            f"-# A verificação automatica foi habilitada novamente!"
        )
        
        return discord.Embed(
            author=self._EmbedAuthor,
            title="APLICAÇÃO OPERANTE! ",
            description=description,
            thumbnail="https://i.postimg.cc/hGMJvhvp/approved.png",
            timestamp=datetime.now(),
            color=3066993,
            footer=self._EmbedFooter
        ).to_dict()
        
    def application_on(self, logs: deque[str], log_positive: str, checked_at: datetime, restarted_at: datetime | None, initialized_at: datetime) -> dict:
        
        restarted_at_text = f" <t:{int(restarted_at.timestamp())}:R>**: <t:{int(restarted_at.timestamp())}:f>." if restarted_at else ":** Negativo."
        description = (
            "A aplicação API Discord Shox foi verificada e está online!\n\n"
            f"- ⏱️ | **Verificada <t:{int(checked_at.timestamp())}:R>**: <t:{int(checked_at.timestamp())}:f>.\n"
            f"- 🔛 | **Rodando <t:{int(initialized_at.timestamp())}:R>**: <t:{int(initialized_at.timestamp())}:f>.\n"
            f"- ♻️ | **Reiniciada{restarted_at_text}\n\n"
            f"{self._add_logs(logs)}"
            f"**REGISTRO POSITIVO:**\n```{log_positive}```"
        )
        
        return discord.Embed(
            author=self._EmbedAuthor,
            title="APLICAÇÃO OPERANTE! ",
            description=description,
            thumbnail="https://i.postimg.cc/hGMJvhvp/approved.png",
            timestamp=datetime.now(),
            color=3066993,
            footer=self._EmbedFooter
        ).to_dict()
        
    def application_off(self, logs: deque[str], checked_at: datetime) -> dict:
        
        description = (
            "A aplicação API Discord Shox foi detectada inoperante!\n\n"
            f"- ⏱️ | **Verificada <t:{int(checked_at.timestamp())}:R>**: <t:{int(checked_at.timestamp())}:f>.\n"
            f"- ♻️ | **Reinicialização:** Em andamento.\n\n"
            f"{self._add_logs(logs)}"
            f"-# A verificação automatica foi desabilitada temporariamente!"
        )
        
        return discord.Embed(
            author=self._EmbedAuthor,
            title="APLICAÇÃO INOPERANTE! ",
            description=description,
            thumbnail=defaultEmbedsInfo["ERROR"]["thumbnail"],
            timestamp=datetime.now(),
            color=14823215,
            footer=self._EmbedFooter
        ).to_dict()
        
    def logger(self, level: str, message: str) -> dict:
        
        return discord.Embed(
            author=self._EmbedAuthor,
            title=defaultEmbedsInfo[level]["title"],
            description=message.split(f'{level} - ')[1],
            color=defaultEmbedsInfo[level]["color"],
            thumbnail=defaultEmbedsInfo[level]["thumbnail"],
            timestamp=datetime.strptime(message.split(" - ")[0], "%Y-%m-%d %H:%M:%S,%f"),
            footer=self._EmbedFooter
        ).to_dict()

    
    def _add_logs(self, logs: deque[str]):
        return (
            "Verifique abaixo os ultimos 10 registros da aplicação.\n\n"
            f"**REGISTROS DA APLICAÇÃO:**\n```{'\n\n'.join(logs)}```\n\n"
        )