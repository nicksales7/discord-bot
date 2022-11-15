import hikari
import lightbulb 
from dotenv import load_dotenv
import json

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]


bot = lightbulb.BotApp(
    token=token, 
    default_enabled_guilds=(1026561071911288932))
    
@bot.listen(hikari.StartedEvent) #Indicates bot has started in terminal
async def bot_started(event):
    print("Bot has started!")

bot.load_extensions_from('./extensions')




bot.run()