import lightbulb 
import hikari
import randfacts

plugin = lightbulb.Plugin('Facts!')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)
    
@plugin.command
@lightbulb.command('facts', 'fact command')
@lightbulb.implements(lightbulb.SlashCommand)
async def subcommand(context):
    x = randfacts.get_fact()
    await context.respond(x)
    
def load(bot):
    bot.add_plugin(plugin)