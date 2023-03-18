from discordwebhook import Discord
import server.firebase as fire
dcurl=fire.dowmdate('Scratch_Online/SOG')['Discord_webhook']
discord = Discord(url=dcurl)
def post(title,description):
  discord.post(embeds=[{"title":title,"description":description,'name':'SOG-Chrome-Addons'}])