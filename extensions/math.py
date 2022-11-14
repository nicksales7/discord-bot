import lightbulb 
import hikari

plugin = lightbulb.Plugin('Math!')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)
    
@plugin.command
@lightbulb.option('num2', 'Last number', type=int)
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.command('add', 'Add two numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):
    await context.respond(context.options.num1 + context.options.num2)
    
def load(bot):
    bot.add_plugin(plugin)