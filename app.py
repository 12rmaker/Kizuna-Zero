#import main discord module
import discord
#discord library has a builtin support for commands
from discord.ext import commands
#import asyncio for asynchronous support
import asyncio
#config module for adding token and meta data 
import config
import fun


#create instance of the discord bot client (main object) from commands module
kizuna = commands.Bot(command_prefix = "?", description = "Kizuna Ai")

#kizuna.event is called when an event or change is detected
@kizuna.event
#in this case the event is on_ready, meaning the bot is ready and connected
async def on_ready():
    '''
    Function definition for when client (kizuna) is ready and connected
    Prints the following to console: Username of bot, ID of bot
    '''
    print("HAI DOMO, logged in as")
    print(kizuna.user.name)
    print(kizuna.user.id)
    print("------")

#kizuna.command is called when a user message has a command
@kizuna.command(description = "Say hi!")
#name of function is name of command due to discord library's nature of parsing
async def hello():
    #use "await" keyword only if a function uses "async" keyword
    await kizuna.say("Hai domo")

@kizuna.command(pass_context = True, description = "Hug another user!")
async def hug(huger,*hugee):
    await fun.hug(discord, kizuna, huger, *hugee)
    

@kizuna.command(description = "Random Kizuna Picture")
async def ai():
    await fun.ai(discord, kizuna)

# initiate the bot with the token as a string
if config.bot_token== "":
    token = input("Input token: ")
    kizuna.run(token)
else:    
    kizuna.run(config.bot_token)
