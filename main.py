import discord
import os
import configparser
import random
from discord.ext import commands


# Read Config.ini File
config = configparser.ConfigParser()
config.read(os.path.abspath(__file__).replace(os.path.basename(__file__), "config.ini"))

# Tokens
DiscordToken = config["Discord"]["discordToken"]

intents = discord.Intents.default()
intents.members = True
intents.messages = True

# Bots Prefix
client = commands.Bot(intents=intents, command_prefix = "$")

# Removes the basic discord Help command
client.remove_command("help")

# Will show that the Bot is online in console
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print(f'{client.user} has logged in')

@client.command()
async def whitevalentine(ctx):
    await ctx.message.delete()    
    prizes = ["肉肉x1 (可赠送给喜欢的陪玩/存入余额)", "专属后缀1周 (可可赠送给喜欢的陪玩)", "开出单人置顶tag 1个月 (可转让)", "开出双人置顶tag 1个月 (可转让)", "私人频道 1个月 (拥有专属权限)", "开出绝版活动Tag: <@&949206743081185330> (可转让)", "开出代金卷$10", "开出代金卷$6", "公会给你报销奶茶 (限额$15)", "陪玩普通半日冠"]
    number = random.choices(prizes, weights=(40,10,6,5,10,10,4,5,8,2), k=1)
    if ctx.channel.id == 948445674599510056: 
        await ctx.send(f"恭喜<@{ctx.message.author.id}>抽到 **{random.choices(prizes, weights=(40,10,6,5,10,10,4,5,8,2), k=1)}**")
    else:
        None

client.run(DiscordToken)