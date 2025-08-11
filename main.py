# Import Libraries
import disnake
from disnake.ext import commands
import api
from datetime import datetime, timezone, timedelta
import asyncio
import asyncpraw
import json
import os

# Command Flags
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

# Bot set
intents = disnake.Intents.default() # Bot Permission
intents.message_content = True

# Don't forget to replace this prefix
client = commands.Bot(
    command_prefix='tb.',
    intents=disnake.Intents.all(),
    status=disnake.Status.online,
    command_sync_flags=command_sync_flags
)

# Import all channels IDs. Make sure to enter your Channel IDs
INFO_WELCOME=1372162402837200896
#INFO_RULES=1372163416051159063
INFO_NEWS=1372162423519449090
INFO_UPD=1372162445858181153
INFO_CONTACTS=1372162543501443142
INFO_MEMES=1372162583859171411
INFO_INVITES=1372162983727206480
APPEAL_SUPPORT=1372165204690862220
APPEAL_COMPLAINT=1372165236915703889
APPEAL_IDEAS=1372165696854687857
FORUM_HELPER=1372163785263157300
FORUM_YT=1372164301489442907
FORUM_TT=1372164323169796096
FORUM_ROLES=1372164567777411172
LOGS=1372163171024113664

# Initialize server_roles as dictionary
server_roles={}

# Game Event
@client.event
async def on_ready():
    game=disnake.Game("Commands Listening")
    await client.change_presence(status=disnake.Status.idle, activity=game)

# Welcome to the server
@client.event
async def on_member_join(member):
    
    channel = client.get_channel(1372162402837200896)
    
    content=member.mention
    embed=disnake.Embed(
        title='Добро пожаловать на дискорд сервер {member.guild}',
        description='Друг, приветствуем тебя на дискорд сервере по обучению работы с Discord Api\n',
        color=disnake.Color(0xFFFFFF) # 
    )
    embed.add_field(
        name='Прежде чем начать, пожалуйста аознакомся с правилами сервера <#1372163416051159063>',
        value='Мы рады, что ты с нами, и надеемся, что твое пребывание здесь будет незабываемым',
        inline=False
    )
    embed.add_field(
        name="Приятного времяпровождения на Discord сервере {member.guild}",
        value="",
        inline=False
    )
    button = disnake.ui.Button(label=f"Вы стали {member.guild.member_count}-м участником!", disabled=True, style=disnake.ButtonStyle.secondary)
    components = disnake.ui.ActionRow(button) # Wrap the button in an ActionRow
    await channel.send(components=components, embed=embed, content=content)

# Bot run

client.run(api.token['DISCORD_API'])
