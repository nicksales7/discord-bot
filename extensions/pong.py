import lightbulb 
import hikari

plugin = lightbulb.Plugin('Pong!')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)
    
@plugin.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Pong!')

def load(bot):
    bot.add_plugin(plugin)