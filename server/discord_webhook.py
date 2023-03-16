from discordwebhook import Discord
discord = Discord( url="https://discord.com/api/webhooks/1085915907274051637/J5JO8IK757EEYpQAr8a_u2mZxi4jtk-lPrAsT8UhMb9F4TocyEWX502To_VLA_9O_xwh")
while True:
  discord.post(content=input('`:'))