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
    
    
@bot.command #Addition command
@lightbulb.option('num2', 'Last number', type=int)
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.command('add', 'Add two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):
    await context.respond(context.options.num1 + context.options.num2)




bot.run()