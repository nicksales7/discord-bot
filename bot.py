import hikari
import lightbulb 
import randfacts

bot = lightbulb.BotApp(
    token="MTA0MTQ3NjkwNzE0Mjc0NjIwMw.Gw4_PH.ObUSRjQ3kQUe_DmyWOv2NGYUmpuJVf03_8R6Sw", 
    default_enabled_guilds=(1026561071911288932))
    
@bot.listen(hikari.StartedEvent) #Indicates bot has started in terminal
async def bot_started(event):
    print("Bot has started!")

bot.load_extensions_from('./extensions')




bot.run()