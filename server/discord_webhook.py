from discordwebhook import Discord
import server.firebase as fire

dcurl = fire.dowmdate('Scratch_Online/SOG')['Discord_webhook']
discord = Discord(url=dcurl)

def send_m(m):
  discord.post(content=m)

def post(title, description):
  discord.post(embeds=[{
    "author": {
      "name": '共帳狀況更新',
      "icon_url": "https://sunocagames.github.io/SunOcaGames/img/sun_logo_%E6%AD%A3%E6%96%B9%E5%BD%A2500.500.png",
    },
    "title": title,
    "description": description,
    "thumbnail": {
      "url": "https://sunocagames.github.io/SunOcaGames/img/Scratch.logo.S.png"
    },
    "footer": {
      "text": "太陽之海遊戲工作室的瀏覽器外掛公用程式",
      "icon_url": "https://sunocagames.github.io/SunOcaGames/img/sun_logo_%E6%AD%A3%E6%96%B9%E5%BD%A2500.500.png",
    },
  }], )
